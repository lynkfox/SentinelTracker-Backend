from __future__ import print_function
from dataclasses import dataclass, field
from auth import get_google_credentials_through_oath2
from common.models.schema_models import (
    GameDetail,
    OblivAeonDetail,
    Username,
    HeroTeam,
    VillainOpponent,
)
from common.models.game_details_enums import GameMode
from common.rds import get_mysql_client
from google_docs.docs_to_enums.character_mapping import *
from googleapiclient.discovery import build
from datetime import datetime


# The ID of a sample document.
DOCUMENT_ID = "1bVppJL4rC5lWULLGZ7AP5xH6YZLYsv86Wme1SpU6agE"
RANGE = "Form Responses 4!A2:AL5"


def main():

    client = get_mysql_client()

    creds = get_google_credentials_through_oath2()

    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=DOCUMENT_ID, range=RANGE).execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return

    for index, row in enumerate(values):
        villain_opponent = map_villain_opponent_team(row, index)
        hero_team = map_hero_team(row, index)
        details = map_row_to_game_details(row, villain_opponent, hero_team, index)

        print(details)


def determine_number_of_heroes(row: list) -> int:
    """
    calculates total heroes in a row
    """

    hero_indexes = [17, 19, 21, 23, 25]
    total = 0
    for index in hero_indexes:
        if HERO_GOOGLE_TO_RDS_MAPPING.get(row[index]) is not None:
            total += 1
    return total


def process_date(date_str) -> str:
    """
    converts the date into a datetime object and adds tz (assumes it is UTC)
    """
    return datetime.strptime(f"{date_str}+00:00", "%d/%m/%Y %h:%m:%s%z")


def map_row_to_game_details(
    row: list, villains: VillainOpponent, heroes: HeroTeam, row_count: int
) -> GameDetail:

    dispatch = {
        "username": (34, USERNAME_CONSOLIDATION),
        "entered_on": (0, process_date),
        "game_mode": "",
        "selection_method": 28,
        "platform": 33,
        "end_result": (16, WIN_CONDITION_GOOGLE_TO_RDS),
        "estimated_time": 30,
        "house_rules": None,
        "number_of_players": 31,
        "number_of_heroes": determine_number_of_heroes,
        "perceived_difficulty": 29,
        "rounds": 32,
        "oblivaeon_details": None,
        # hero_team
        "environment": (27, ENVIRONMENT_GOOGLE_TO_RDS_MAP),
        # villain
        "hero_one_incapped": 18,
        "hero_two_incapped": 20,
        "hero_three_incapped": 22,
        "hero_four_incapped": 24,
        "hero_five_incapped": 26,
        "villain_one_incapped": (3, 12),
        "villain_two_incapped": 5,
        "villain_three_incapped": 7,
        "villain_four_incapped": 9,
        "villain_five_incapped": 11,
    }
    details = {}
    for key, index in dispatch.items():
        if isinstance(index, int):
            value = row[index]
            if "incapped" in key:
                value = value == "" or value is None
            details[key] = value
        elif index == "":
            details[key] = GameMode.NORMAL.value

        elif isinstance(index, tuple):

            if isinstance(index[1], dict):
                details[key] = index[1].get(row[index[0]])
            elif isinstance(index[1], function):
                details[key] = index(row[index[0]])

        elif isinstance(index, function):
            details[key] = index(row)

        else:
            details[key] = index

        if key not in ["house_rules", "oblivaeon_details"] and details[key] is None:
            print(
                f"Row {row_count}: (kwarg key: row value) -> ({key}:{row[index]}) evaluated to NONE "
            )

    details["hero_team"] = heroes
    details["villain"] = villains

    return GameDetail(**details)


def map_villain_opponent_team(row: list, row_count: int) -> VillainOpponent:
    """
    Maps rows to dictionaries and into VillainOpponent pydantic Base Model for use in Inserting into RDS
    """

    dispatch = {
        "villain_one": (1, 2),
        "villain_two": 4,
        "villain_three": 6,
        "villain_four": 8,
        "villain_five": 10,
        "id_hash": None,
    }

    opponent_team = {}
    for key, index in dispatch.items():
        if isinstance(index, int):
            opponent_team[key] = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index])
        elif isinstance(index, tuple):
            opponent_team[key] = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[0]])
            if opponent_team[key] == None:
                opponent_team[key] = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[1]])
        else:
            opponent_team[key] = index

        if key != "id_hash" and opponent_team[key] is None and row[index] != "":
            print(f"Row {row_count}: key ({key}:{row[index]}) evaluated to NONE ")

    return VillainOpponent(**opponent_team)


def map_hero_team(row: list, row_count: int) -> HeroTeam:

    dispatch = {
        "hero_one": 17,
        "hero_two": 19,
        "hero_three": 21,
        "hero_four": 23,
        "hero_five": 25,
        "id_hash": None,
    }
    hero_team = {}
    for key, index in dispatch.items():
        if isinstance(index, int):
            hero_team[key] = HERO_GOOGLE_TO_RDS_MAPPING.get(row[index])
        else:
            hero_team[key] = index

        if key != "id_hash" and hero_team[key] is None and row[index] != "":
            print(
                f"Row {row_count}: (kwarg key: row value) -> ({key}:{row[index]}) evaluated to NONE "
            )

    return HeroTeam(**hero_team)


if __name__ == "__main__":
    main()
