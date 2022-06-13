from auth import get_mysql_client
from google_docs.google_aws_common import SqlColumns, SqlTables
from common.models.enums import BoxSet
import json


def main():
    """
    First time script after tables are created, run this to insert the base game data
    """
    client = get_mysql_client()
    cursor = client.cursor()
    insert_box_sets(cursor)

    client.commit()


def insert_box_sets(cursor):
    sql = f"INSERT INTO {SqlTables.BOX_SETS} ({SqlColumns.FULL_NAME}, {SqlColumns.DYNAMO_META}) VALUES (%s, %s)"
    values = [
        (
            member.value,
            json.dumps({"pk": f"BOX_SET#{_clean_name(member.value.upper())}", "sk": "META#BOX_SET"}),
        )
        for member in BoxSet
    ]
    cursor.executemany(sql, values)

def insert_villains(cursor):
    

def _clean_name(name:str) -> str:
    specialChars = " :-'()" 
    for char in specialChars:
        name = name.replace(char, "_")
    return name


if __name__ == "__main__":
    main()
