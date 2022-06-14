from typing import Union
from common.models.character_enums import (
    Character,
    AlternateTags,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)
import boto3
import json
from common.models.enums import SqlTables
import mysql.connector


def get_mysql_client():

    client = boto3.client("secretsmanager")

    response = client.get_secret_value(
        SecretId="statisticsrdsSecret27E3DF08-7PVhSz2tbcfc"
    )

    secrets = json.loads(response["SecretString"])

    return mysql.connector.connect(
        host=secrets["host"],
        user=secrets["username"],
        password=secrets["password"],
        database=SqlTables.STATISTICS_DB_NAME,
    )


def create_rds_key(
    full_name: Union[Character, str],
    alternate_name: Union[AlternateTags, str, None],
    mapping: dict,
) -> str:
    """
    Builds the "full_name" for a given Hero, Villain, or Environment entry in the RDS
    """
    alternate_name = ALTERNATE_TAG_DISPLAY_MAPPING.get(alternate_name)
    full_name = mapping.get(full_name)
    if alternate_name is not None:
        full_name = f"{full_name}{alternate_name}"

    return full_name
