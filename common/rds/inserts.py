from common.models.schema_models import GameDetail, HeroTeam, VillainOpponent, OblivAeonDetail, User
from typing import Union
from aws_lambda_powertools import Logger

logger = Logger()


def insert(sql_client, model: Union[GameDetail, HeroTeam, VillainOpponent, OblivAeonDetail, User]) -> bool:
    try:
        sql_insert_statement = model.get_insert_statement()
        sql_client.cursor().execute(sql_insert_statement)
        sql_client.commit()

    except Exception as e:
        if e.errno == 1062:
            logger.debug("Item already exists. Skipping insert", extra=model.dict())
            pass
        else:
            logger.exception("Error in attempting to insert", extra=model.dict())
