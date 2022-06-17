from py_linq import Enumerable
import models
from common.rds import LookUp, Operation
from common.models.schema_models import GameDetail
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition
from typing import List


def calculate(request: LookUp, response: List[GameDetail]) -> models.StatisticsResponse:
    """
    Calculates the various statistics for a given request
    """

    # py-linq Enumerable, for using LINQ style syntax
    collection = Enumerable(response)


def _is_win_condition(end_result: str) -> bool:
    return any([end_result == (win_condition.value if isinstance(end_result, str) else win_condition) for win_condition in HeroWinCondition])
