from __future__ import print_function
from google_docs.google_aws_common import SqlColumns, SqlTables
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
from dateutil.parser import parse
from time import perf_counter


# The ID of a sample document.
DOCUMENT_ID = "1bVppJL4rC5lWULLGZ7AP5xH6YZLYsv86Wme1SpU6agE"
RANGE = "Form Responses 4!A2:AL"


def main():

    print("** Establishing Connections ...")
    client = get_mysql_client()

    creds = get_google_credentials_through_oath2()

    start = perf_counter()
    service = build("sheets", "v4", credentials=creds)

    print("** Pulling data from Google ...")
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=DOCUMENT_ID, range=RANGE).execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return
    end_get = perf_counter()

    print("** Parsing data (each dot is 1000 entries parsed) ...")
    details = [map_row_to_game_details(row, index) for index, row in enumerate(values)]

    end_parse = perf_counter()

    print("\n** Creating Insert Statements ...")
    user_sql_statement = f"INSERT INTO {SqlTables.USERS} ({SqlColumns.USERNAME}, {SqlColumns.DYNAMO_META}) VALUES (%s, %s)"
    user_values = list(
        set(
            [
                create_values_for_user_insert(detail.username)
                for detail in details
                if detail is not None and detail.username is not None
            ]
        )
    )

    # need to remove Nones and duplicates from above list.
    end_statement = perf_counter()

    print("** Inserting into SQL DB ...")

    end_insert = perf_counter()
    print(
        f"\n{len(values)} entries retrieved in {end_get-start} seconds"
        f"\n ..... parsed in {end_parse-end_get} seconds"
        f"\n ..... insert statements created in {end_statement-end_parse} seconds"
        f"\n ..... inserted in {end_insert-end_statement} seconds"
        f"\n\n *Complete. {len(user_values)} Users and x Game data inserted in {end_insert-start} total seconds "
    )


def create_values_for_user_insert(user: Username) -> set:
    if user.username != "":
        return (user.username, user.dynamo_meta_query)


def determine_number_of_heroes(row: list) -> int:
    """
    calculates total heroes in a row
    """

    hero_indexes = [17, 19, 21, 23, 25]
    total = 0
    for index in hero_indexes:

        if len(row) > index and HERO_GOOGLE_TO_RDS_MAPPING.get(row[index]) is not None:
            total += 1
    return total


def process_date(date_str) -> str:
    """
    converts the date into a datetime object and adds tz (assumes it is UTC)
    """
    return parse(f"{date_str}+00:00")


def map_row_to_game_details(row: list, row_count: int) -> GameDetail:

    dispatch = {
        "username": (34, USERNAME_CONSOLIDATION),
        "entered_on": (0, process_date),
        "game_mode": "",
        "selection_method": (28, SELECTION_METHOD_GOOGLE_TO_RDS),
        "platform": (33, PLATFORM_GOOGLE_TO_RDS),
        "end_result": (16, WIN_CONDITION_GOOGLE_TO_RDS),
        "estimated_time": (30, GAME_LENGTH_GOOGLE_TO_RDS),
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
        "comment": 35,
    }
    details = {}
    for key, index in dispatch.items():
        if isinstance(index, int):
            value = row[index] if index < len(row) else ""
            if "incapped" in key:
                value = value != ""

            if key == "estimated_time" and value == "":
                value = "Unknown"

            if key == "rounds":
                try:
                    value = abs(int(value))
                except Exception:
                    value = 0

            if key in ["number_of_players", "perceived_difficulty"] and value == "":
                value = -1

        elif index == "":
            value = GameMode.NORMAL.value

        elif isinstance(index, tuple):

            if isinstance(index[1], dict):
                google_value = row[index[0]].strip() if index[0] < len(row) else ""
                value = index[1].get(google_value)
                if key == "username":

                    value = Username(
                        **{
                            "username": google_value if value is None else value,
                            "dynamo_meta_query": None,
                            "total_wins": 0,
                            "total_games": 0,
                        }
                    )

            elif callable(index[1]):
                value = index[1](row[index[0]])

        elif callable(index):
            value = index(row)

        else:
            value = index

        details[key] = value
        if key not in ["house_rules", "oblivaeon_details"] and details[key] is None:
            if isinstance(index, tuple):
                google_value = row[index[0]] if len(row) > index[0] else ""
            else:
                google_value = row[index]

    details["hero_team"] = map_hero_team(row)
    if details["hero_team"] is None:
        return None
    details["villain"] = map_villain_opponent_team(row)

    if row_count % 1000 == 0:
        print(".", end=" ")
    return GameDetail(**details)


def map_villain_opponent_team(row: list) -> VillainOpponent:
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
            value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index])
        elif isinstance(index, tuple):
            value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[0]])
            if value == None:
                value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[1]])
        else:
            value = index

        opponent_team[key] = value

    return VillainOpponent(**opponent_team)


def map_hero_team(row: list) -> HeroTeam:

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
            hero_team[key] = (
                HERO_GOOGLE_TO_RDS_MAPPING.get(row[index]) if len(row) > index else None
            )
        else:
            hero_team[key] = index

    if hero_team["hero_three"] is None:
        return None

    return HeroTeam(**hero_team)


if __name__ == "__main__":
    main()
