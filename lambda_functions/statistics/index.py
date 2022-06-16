import json
import os

import boto3
from aws_lambda_powertools import Logger
from models import Statistics
from common.rds.queries import query_

logger = Logger()

DYNAMO_RESOURCE = boto3.resource("dynamodb")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE_NAME")


@logger.inject_lambda_context(log_event=True, clear_state=True)
def lambda_handler(event: dict, context: dict) -> dict:
    """
    Handles all routing of the api, based on path.
    """

    try:

        _event = Statistics(event)
        body = {"message": "Invalid format"}

        if _event.IS_OPTIONS:
            body = {"message": "Preflight Accepted"}

        if _event.IS_GET:
            body = query_(_event.look_up_data.operations)

    except Exception as e:
        logger.exception("Unhandled Error")
        body = {"message": "Error'd", "errorMessage": str(e)}

    finally:
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET",
            },
            "body": json.dumps(body),
        }
