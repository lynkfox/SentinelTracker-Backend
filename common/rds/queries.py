from common.rds import Operation
from typing import List
from common.models.schema_models import GameDetail
from common.rds.queries_gen import generate_from_operations
from aws_lambda_powertools import Logger

logger = Logger()


def query(operations: List[Operation], my_sql_client: any) -> List[GameDetail]:
    """
    Builds a query and makes a call to the RDS. Returns the results as a list
    of QueryResult models
    """

    query_string = generate_from_operations(operations).replace("'s", "\\'s")

    logger.debug("Query String", extra={"query_string": query_string})
    cursor = my_sql_client.cursor()
    cursor.execute(query_string)
    response_rows = cursor.fetchall()
    logger.debug("Top response from query", extra={"response_first_row": str(response_rows[0])})
    return [map_row_to_GameDetails(row) for row in response_rows]


def map_row_to_GameDetails(row: tuple) -> dict:
    """
    maps a query response to a dictionary compatible with GameDetails base
    model.
    """
    key_values = {key: row[i + 1] for i, key in enumerate(GameDetail.__fields__)}

    return GameDetail(**key_values)
