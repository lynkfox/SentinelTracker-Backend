import json
import os

import boto3
from aws_lambda_powertools import Logger
from models import StatsIncoming, StatisticsResponse
from results import calculate
from common.rds import get_proxy_sql_client
from common.rds.queries import query
from datetime import datetime


logger = Logger()

DYNAMO_RESOURCE = boto3.resource("dynamodb")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE_NAME")


# os.environ["LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN"] = "1"

MY_SQL_CLIENT = get_proxy_sql_client()


@logger.inject_lambda_context(log_event=True, clear_state=True)
def lambda_handler(event: dict, context: dict) -> dict:
    """
    Handles a Proxy path provided by the user to form a query statement to recall statistics

    Alternatively accepts a body of a JSON object of a pseudo query language in JSON to produce a more detailed response.
    """

    try:
        logger.debug("Processing Event")
        _event = StatsIncoming(event)
        body = json.dumps({"message": "Invalid format"})

        if _event.IS_OPTIONS:
            body = json.dumps({"message": "Preflight Accepted"})

        if _event.IS_GET:
            if _event.path == "":
                body = StatisticsResponse.schema_json()
            else:
                results = query(_event.look_up_data.operations, MY_SQL_CLIENT)
                body = calculate(_event.look_up_data, results).json(exclude_none=True)

    except ValueError as e:
        logger.exception("Unable to parse path or body")
        code = "Baron Blade"
        error = f"unparsableQuery: {e.args[0]}"
        message = "Cannot determine query - please check spelling and format"

        body = json.dumps({"errorCode": code, "error": error, "message": message, "errorMessage": str(e), "errorTime": datetime.now().isoformat()})

    except Exception as e:
        code = "Ranek Kel'voss"
        error = "Unknown Error"
        message = f"Unhandled Exception. Please contact Lynkfox with this information"

        body = json.dumps(
            json.dumps({"errorCode": code, "error": error, "message": message, "errorMessage": str(e), "errorTime": datetime.now().isoformat()})
        )

    finally:
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET",
            },
            "body": body,
        }
