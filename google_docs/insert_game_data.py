from common.rds import get_mysql_client
from google_docs.google_aws_common import SqlColumns, SqlTables
from common.models.game_details_enums import BoxSet
from inserts.insert_environments import ENVIRONMENTS_TO_INSERT
from inserts.insert_heroes import HEROES_TO_INSERT
from inserts.insert_villains import VILLAINS_TO_INSERT
import json


def main():
    """
    First time script after tables are created, run this to insert the base game data
    """
    client = get_mysql_client()
    # Uncomment a particular block to insert the base values into the table for the first time.

    print("Inserting Box Sets...")
    cursor = client.cursor()
    insert_box_sets(cursor)
    client.commit()
    print(f"{cursor.rowcount} BoxSet records inserted.")

    print("Inserting Villains")
    cursor = client.cursor()
    insert_entities(cursor, SqlTables.VILLAINS, create_values(VILLAINS_TO_INSERT))
    client.commit()
    print(f"{cursor.rowcount} Villain records inserted.")

    print("Inserting Heroes")
    cursor = client.cursor()
    insert_entities(cursor, SqlTables.HEROES, create_values(HEROES_TO_INSERT))
    client.commit()
    print(f"{cursor.rowcount} Hero records inserted.")

    print("Inserting Environments")
    cursor = client.cursor()
    insert_entities(
        cursor, SqlTables.ENVIRONMENTS, create_values(ENVIRONMENTS_TO_INSERT)
    )
    client.commit()
    print(f"{cursor.rowcount} Environment records inserted.")

    print("All Done")


def insert_box_sets(cursor):
    sql = f"INSERT INTO {SqlTables.BOX_SETS} ({SqlColumns.FULL_NAME}, {SqlColumns.DYNAMO_META}) VALUES (%s, %s)"
    values = [
        (
            member.value,
            json.dumps(
                {"pk": f"{_clean_name(member.value.upper())}#BOX_SET", "sk": "META#"}
            ),
        )
        for member in BoxSet
    ]
    cursor.executemany(sql, values)


def insert_entities(cursor, table, values):
    sql = f"INSERT INTO {table} ({SqlColumns.FULL_NAME}, {SqlColumns.BOX_SET}, {SqlColumns.DYNAMO_META}) VALUES (%s, %s, %s)"
    cursor.executemany(sql, values)


def create_values(entities: list):
    return [
        (entity.full_name, entity.box_set, entity.dynamo_meta_query)
        for entity in entities
    ]


def _clean_name(name: str) -> str:
    specialChars = " :-'()"
    for char in specialChars:
        name = name.replace(char, "_")
    return name.replace("__", "_")


if __name__ == "__main__":
    main()
