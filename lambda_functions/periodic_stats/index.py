import os
import json

import boto3
from aws_lambda_powertools import Logger
from entry_models import GameDetailIncoming
from common.models.schema_models import GameDetail
from common.rds import get_proxy_sql_client
from periodic_utilities import get_all_GameDetails_as_enumerable
from datetime import datetime
from py_linq import Enumerable


logger = Logger()

DYNAMO_RESOURCE = boto3.resource("dynamodb")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE_NAME")


# os.environ["LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN"] = "1" - currently set in common.rds

MY_SQL_CLIENT = get_proxy_sql_client()


@logger.inject_lambda_context(log_event=True, clear_state=True)
def lambda_handler(event: dict, context: dict) -> dict:
    """
    Runs once per day to periodically build interesting statistics
    """
    all_details = get_all_GameDetails_as_enumerable(MY_SQL_CLIENT)
