import os
import json

import boto3
from aws_lambda_powertools import Logger
from entry_models import GameDetailIncoming
from common.models.schema_models import GameDetail
from common.rds import get_proxy_sql_client
from common.rds.inserts import insert
from datetime import datetime
from common.security.api import check_approved_preflight_cors


logger = Logger()

DYNAMO_RESOURCE = boto3.resource("dynamodb")
DYNAMO_TABLE = os.getenv("DYNAMO_TABLE_NAME")


# os.environ["LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN"] = "1" - currently set in common.rds

MY_SQL_CLIENT = get_proxy_sql_client()


@logger.inject_lambda_context(log_event=True, clear_state=True)
def lambda_handler(event: dict, context: dict) -> dict:
    """
    Handles all input of games from any source. Will be behind an API Key as well.
    """
    try:
        logger.debug("Processing Event")
        _event = GameDetailIncoming(event)
        body = json.dumps({"message": "Invalid format"})

        if _event.IS_OPTIONS:
            logger.debug("OPTIONS triggered")
            check_approved_preflight_cors(event)

            body = json.dumps({"message": "Preflight Accepted"})

        elif _event.IS_GET:
            logger.debug("GET triggered")
            body = GameDetail.schema_json()

        elif _event.IS_POST:
            logger.debug("POST triggered")
            if _event.entry_data is None:
                raise ValueError("Missing")
            if _event.entry_data.entry_is_valid is False and _event.entry_data.house_rules is False:
                raise ValueError("NotHouseRuled")

            if insert(MY_SQL_CLIENT, _event.entry_data) is True:
                body = {"message": "Data successfully added", "code": "Legacy", "dataEntered": _event.entry_data.dict()}

    except ValueError as e:
        logger.info("error!", exc_info=True)
        code = "Omnitron"
        error = "ValueError"
        message = f"Unknown Value Error"

        if e.args[0] == "NotHouseRuled":
            code = "Ermine"
            error = "InvalidData"
            message = "One or more inputs has made this an invalid game set up. If this was intentional, please ensure that 'house_rules' is set to True and re-submit. Please note these games will not be counted in the official response statistics. It is highly recommended you add a comment explaining your house rules."

        if e.args[0] == "Missing":
            code = "Ambuscade"
            error = "MissingData"
            message = "Add Game Entry call with no body"

        body = {"errorCode": code, "error": error, "message": message, "errorMessage": str(e), "errorTime": datetime.now().isoformat()}
        logger.debug("Value Error", extra=body, exc_info=True)

    except Exception as e:
        code = "OblivAeon"
        error = "Unknown Error"
        message = f"Unhandled Exception. Please contact Lynkfox with this information"

        body = {"errorCode": code, "error": error, "message": message, "errorMessage": str(e), "errorTime": datetime.now().isoformat()}
        logger.debug("Unknown Error", extra=body, exc_info=True)

    finally:
        if isinstance(body, dict):
            body = json.dumps(body)
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,GET,POST",
            },
            "body": body,
        }
