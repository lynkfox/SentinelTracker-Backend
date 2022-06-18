from common.rds import get_mysql_client
from common.sql_attributes import SqlColumns, SqlTables
from common.models.game_details_enums import BoxSet
from inserts.insert_environments import ENVIRONMENTS_TO_INSERT
from inserts.insert_heroes import HEROES_TO_INSERT
from inserts.insert_villains import VILLAINS_TO_INSERT
from inserts.insert_rook_city_renegades import RENEGADE_ENVIRONMENT_INSERTS, RENEGADE_HERO_INSERTS, RENEGADE_VILLAIN_INSERTS
import json


def main():
    """
    First time script after tables are created, run this to insert the base game data
    """
    client = get_mysql_client()
    # Uncomment a particular block to insert the base values into the table for the first time.

    print("Inserting Villains")
    cursor = client.cursor()
    insert_entities(cursor, SqlTables.VILLAINS, create_values([*VILLAINS_TO_INSERT, *RENEGADE_VILLAIN_INSERTS]))
    client.commit()
    print(f"{cursor.rowcount} Villain records inserted.")

    print("Inserting Heroes")
    cursor = client.cursor()
    insert_entities(cursor, SqlTables.HEROES, create_values([*HEROES_TO_INSERT, *RENEGADE_HERO_INSERTS]))
    # client.commit()
    print(f"{cursor.rowcount} Hero records inserted.")

    print("Inserting Environments")
    cursor = client.cursor()
    insert_entities(cursor, SqlTables.ENVIRONMENTS, create_values([*ENVIRONMENTS_TO_INSERT, *RENEGADE_ENVIRONMENT_INSERTS]))
    client.commit()
    print(f"{cursor.rowcount} Environment records inserted.")

    print("All Done")


def insert_entities(cursor, table, values):
    sql = f"INSERT INTO {table} ({SqlColumns.FULL_NAME}, {SqlColumns.BASE}, {SqlColumns.QUERY_NAME}, {SqlColumns.QUERY_ALT}) VALUES (%s, %s, %s, %s)"
    cursor.executemany(sql, values)


def create_values(entities: list):
    return [(entity.full_name, entity.base, entity.query_name_value, entity.query_alt_value) for entity in entities]


def _clean_name(name: str) -> str:
    specialChars = " :-'()"
    for char in specialChars:
        name = name.replace(char, "_")
    return name.replace("__", "_")


if __name__ == "__main__":
    main()
