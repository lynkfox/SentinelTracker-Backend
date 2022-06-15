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
    details = list(
        filter(
            None,
            [map_row_to_game_details(row, index) for index, row in enumerate(values)],
        )
    )

    end_parse = perf_counter()

    print("\n** Creating Insert Statements ...")
    user_sql_statement = f"INSERT INTO {SqlTables.USERS} ({SqlColumns.USERNAME}, {SqlColumns.DYNAMO_META}) VALUES (%s, %s)"
    user_values = list(
        filter(
            None,
            list(
                set(
                    [
                        create_values_for_user_insert(detail.username)
                        for detail in details
                        if detail is not None and detail.username is not None
                    ]
                )
            ),
        )
    )
    blank_user_sql = f"INSERT {SqlTables.USERS} ({SqlColumns.USERNAME}, {SqlColumns.DYNAMO_META}) VALUES ('', '')"

    hero_team_columns = [
        SqlColumns.ID_HASH,
        SqlColumns.HERO_ONE,
        SqlColumns.HERO_TWO,
        SqlColumns.HERO_THREE,
        SqlColumns.HERO_FOUR,
        SqlColumns.HERO_FIVE,
        SqlColumns.VALID_TEAM,
    ]

    hero_team_sql_statement = f"INSERT INTO {SqlTables.HERO_TEAMS} ({','.join(hero_team_columns)}) VALUES ({insert_value_shortcut(hero_team_columns)})"
    hero_team_values = list(
        set([create_values_for_hero_insert(detail.hero_team) for detail in details])
    )

    opponent_columns = [
        SqlColumns.ID_HASH,
        SqlColumns.VILLAIN_ONE,
        SqlColumns.VILLAIN_TWO,
        SqlColumns.VILLAIN_THREE,
        SqlColumns.VILLAIN_FOUR,
        SqlColumns.VILLAIN_FIVE,
        SqlColumns.VALID_TEAM,
    ]

    opponents_sql_statement = f"INSERT INTO {SqlTables.OPPONENTS} ({','.join(opponent_columns)}) VALUES ({insert_value_shortcut(opponent_columns)})"
    opponent_team_values = list(
        set(
            [
                create_values_for_opponent_team_insert(detail.villain)
                for detail in details
            ]
        )
    )

    game_details_column_names = [
        SqlColumns.USERNAME,
        SqlColumns.ENTER_DATE,
        SqlColumns.GAME_MODE,
        SqlColumns.SELECTION_METHOD,
        SqlColumns.PLATFORM,
        SqlColumns.END_RESULT,
        SqlColumns.ESTIMATED_TIME,
        SqlColumns.HOUSE_RULES,
        SqlColumns.NUMBER_OF_PLAYERS,
        SqlColumns.NUMBER_OF_HEROES,
        SqlColumns.PERCEIVED_DIFFICULTY,
        SqlColumns.ROUNDS,
        SqlColumns.OBLIVAEON_DETAIL,
        SqlColumns.HERO_TEAM,
        SqlColumns.ENVIRONMENT,
        SqlColumns.VILLAIN,
        SqlColumns.HERO_ONE,
        SqlColumns.H1_INCAP,
        SqlColumns.HERO_TWO,
        SqlColumns.H2_INCAP,
        SqlColumns.HERO_THREE,
        SqlColumns.H3_INCAP,
        SqlColumns.HERO_FOUR,
        SqlColumns.H4_INCAP,
        SqlColumns.HERO_FIVE,
        SqlColumns.H5_INCAP,
        SqlColumns.VILLAIN_ONE,
        SqlColumns.V1_INCAP,
        SqlColumns.VILLAIN_TWO,
        SqlColumns.V2_INCAP,
        SqlColumns.VILLAIN_THREE,
        SqlColumns.V3_INCAP,
        SqlColumns.VILLAIN_FOUR,
        SqlColumns.V4_INCAP,
        SqlColumns.VILLAIN_FIVE,
        SqlColumns.V5_INCAP,
        SqlColumns.ENTRY_IS_VALID,
    ]

    game_details_sql_statement = f"INSERT INTO {SqlTables.GAME_DETAILS} ({', '.join(game_details_column_names)}) VALUES ({insert_value_shortcut(game_details_column_names)})"
    game_details_values = list(
        set([create_values_for_game_details_insert(detail) for detail in details])
    )

    end_statement = perf_counter()

    print("*** Inserting into SQL DB ...")

    print("  * Inserting Users")
    client.cursor().execute(blank_user_sql)

    client.cursor().executemany(user_sql_statement, user_values)
    client.commit()

    print("  * Inserting Positionally Unique Hero Teams")

    client.cursor().executemany(hero_team_sql_statement, hero_team_values)
    client.commit()

    print("  * Inserting Positionally Unique Opponent Teams")

    client.cursor().executemany(opponents_sql_statement, opponent_team_values)
    client.commit()

    print("  * Inserting all game details")

    client.cursor().executemany(game_details_sql_statement, game_details_values)
    client.commit()

    end_insert = perf_counter()
    print(
        f"\n{len(values)} entries retrieved in {end_get-start} seconds"
        f"\n ..... parsed in {end_parse-end_get} seconds"
        f"\n ..... insert statements created in {end_statement-end_parse} seconds"
        f"\n ..... inserted in {end_insert-end_statement} seconds"
        f"\n\n *Complete."
        f"\n   - {len(user_values)} Users added."
        f"\n   - {len(hero_team_values)} Unique Hero Team setups added."
        f"\n   - {len(opponent_team_values)} Unique Opponent Team setups added."
        f"\n   - {len(game_details_values)} Game data inserted."
        f"\n in {end_insert-start} total seconds "
    )


def insert_value_shortcut(columns):
    string_of_percents = ""
    for i in range(len(columns)):
        string_of_percents += "%s, "
    return string_of_percents[:-2]


def create_values_for_user_insert(user: Username) -> set:
    if user.username != "":
        return (user.username, user.dynamo_meta_query)


def create_values_for_hero_insert(hero_team: HeroTeam) -> set:
    return (
        str(hero_team.id_hash),
        hero_team.hero_one,
        hero_team.hero_two,
        hero_team.hero_three,
        hero_team.hero_four,
        hero_team.hero_five,
        hero_team.valid_team,
    )


def create_values_for_opponent_team_insert(villain: VillainOpponent) -> set:
    return (
        str(villain.id_hash),
        villain.villain_one,
        villain.villain_two,
        villain.villain_three,
        villain.villain_four,
        villain.villain_five,
        villain.valid_team,
    )


def create_values_for_game_details_insert(game: GameDetail) -> set:
    return (
        game.username.username,
        game.entered_on,
        game.game_mode,
        game.selection_method,
        game.platform,
        game.end_result,
        game.estimated_time,
        game.house_rules,
        game.number_of_players,
        game.number_of_heroes,
        game.perceived_difficulty,
        game.rounds,
        game.oblivaeon_details,
        str(game.hero_team.id_hash),
        game.environment,
        str(game.villain.id_hash),
        game.hero_one,
        game.hero_one_incapped,
        game.hero_two,
        game.hero_two_incapped,
        game.hero_three,
        game.hero_three_incapped,
        game.hero_four,
        game.hero_four_incapped,
        game.hero_five,
        game.hero_five_incapped,
        game.villain_one,
        game.villain_one_incapped,
        game.villain_two,
        game.villain_two_incapped,
        game.villain_three,
        game.villain_three_incapped,
        game.villain_four,
        game.villain_four_incapped,
        game.villain_five,
        game.villain_five_incapped,
        game.entry_is_valid,
    )


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


def is_true(value) -> bool:
    """
    converts Yes and No to True and False
    """
    return value.lower() == "yes"


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
            value = GameMode.NORMAL

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

    details["hero_team"], heroes = map_hero_team(row)
    if details["hero_team"] is None:
        return None

    details["hero_one"] = heroes["hero_one"]
    details["hero_two"] = heroes["hero_two"]
    details["hero_three"] = heroes["hero_three"]
    details["hero_four"] = heroes["hero_four"]
    details["hero_five"] = heroes["hero_five"]

    details["villain"], villains = map_villain_opponent_team(row)

    details["villain_one"] = villains["villain_one"]
    details["villain_two"] = villains["villain_two"]
    details["villain_three"] = villains["villain_three"]
    details["villain_four"] = villains["villain_four"]
    details["villain_five"] = villains["villain_five"]

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
        "advanced": (13, is_true),
        "challenge": (14, is_true),
        "id_hash": None,
    }

    opponent_team = {}
    for key, index in dispatch.items():
        if isinstance(index, int):
            value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index])
        elif isinstance(index, tuple):
            if isinstance(index[1], int):
                value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[0]])
                if value == None:
                    value = VILLAIN_GOOGLE_TO_RDS_MAP.get(row[index[1]])
            else:
                value = index[1](row[index[0]])
        else:
            value = index

        opponent_team[key] = value

    opponent = VillainOpponent(**opponent_team)
    return opponent, opponent_team


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
        return None, None

    heroes = HeroTeam(**hero_team)
    return heroes, hero_team


if __name__ == "__main__":
    main()
