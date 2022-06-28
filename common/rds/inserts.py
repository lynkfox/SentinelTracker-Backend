from common.models.schema_models import GameDetail, HeroTeam, VillainOpponent, OblivAeonDetail, User
from typing import Union
from aws_lambda_powertools import Logger

logger = Logger()


def insert(sql_client, model: Union[GameDetail, HeroTeam, VillainOpponent, OblivAeonDetail, User]) -> bool:
    try:

        if isinstance(model, GameDetail):
            insert(sql_client, model.hero_team)
            insert(sql_client, model.villain)

        sql_insert_statement = model.get_insert_statement()
        sql_client.cursor().execute(sql_insert_statement)
        sql_client.commit()

        return True

    except Exception as e:
        return handle_duplicate(model, e)


def handle_duplicate(model, e):
    if hasattr(e, "errno") and e.errno == 1062:
        logger.debug("Item already exists. Skipping insert", extra=model.dict())
        return True
    else:
        logger.exception("Error in attempting to insert", extra={**model.dict(), **{"sql_statement": model.get_insert_statement()}})
        return True
