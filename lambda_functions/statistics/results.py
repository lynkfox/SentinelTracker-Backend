from py_linq import Enumerable
import models
from common.rds import LookUp, Operation
from common.rds.queries import parse_for_rds_names
from common.models.schema_models import GameDetail
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition
from typing import List


def calculate(request: LookUp, response: List[GameDetail]) -> models.StatisticsResponse:
    """
    Calculates the various statistics for a given request
    """

    # py-linq Enumerable, for using LINQ style syntax
    collection = Enumerable(response)

    requested_parameters = describe_query_parameters(request.operations)

    if requested_parameters.heroes is None or len(requested_parameters.heroes) == 0:
        # include AgainstStatistics for each Hero
        pass

    if requested_parameters.villains is None or len(requested_parameters.villains) == 0:
        # include AgainstStatistics for each Villain
        pass

    if requested_parameters.locations is None or len(requested_parameters.locations) == 0:
        # include InStatistics for each environment
        pass

    if len(requested_parameters.heroes) == 1:
        # include WithStatistics for each other Hero
        pass

    if len(requested_parameters.villains) == 1:
        # include With statistics for each other Villain
        pass

    total_games = len(response)
    total_wins = collection.where(lambda x: _is_win_condition(x.end_result))

    # temp
    stats = models.Statistics(TotalGames=total_games, TotalWins=total_wins)

    return models.StatisticsResponse(RequestedSet=requested_parameters, Statistics=stats)


def describe_query_parameters(operations=List[Operation]) -> models.RequestedSet:
    """
    parses the operations to provide a response of all the parameters in
    an easy to access form
    """

    heroes, opponents, locations, username = parse_for_rds_names(operations)

    return models.RequestedSet(heroes=heroes, villains=opponents, environment=locations, user=username)


def _is_win_condition(end_result: str) -> bool:
    return any([end_result == (win_condition.value if isinstance(end_result, str) else win_condition) for win_condition in HeroWinCondition])
