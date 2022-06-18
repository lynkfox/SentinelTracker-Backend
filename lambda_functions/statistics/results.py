from py_linq import Enumerable
import models
from common.rds import LookUp, Operation
from common.rds.queries_gen import parse_for_rds_names
from common.models.schema_models import GameDetail
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition
from typing import List, Dict


def calculate(request: LookUp, response: List[GameDetail]) -> models.StatisticsResponse:
    """
    Calculates the various statistics for a given request
    """

    # py-linq Enumerable, for using LINQ style syntax
    collection = Enumerable(response)

    requested_parameters = describe_query_parameters(request.operations)
    total_games = len(response)
    total_wins = collection.where(lambda x: _is_win_condition(x.end_result)).count()

    if (requested_parameters.heroes is None or len(requested_parameters.heroes) == 0) and len(requested_parameters.villains) >= 1:

        # Build Solo Villain or Villain Team response:
        #   - includes: Villain stats, Against Other Heroes
        #   - mutually exclusive to the next function
        stats = models.OpponentStatistics(TotalGames=total_games, TotalWins=total_wins, Versus=build_related_hero_stats(collection))

    if requested_parameters.villains is None or len(requested_parameters.villains) == 0 and len(requested_parameters.heroes) >= 1:
        # Build Hero and Hero Team response:
        #   - includes: Hero/Team stats and against villains
        #   - mutual exclusive to the one above.
        pass

    if requested_parameters.environment is None or len(requested_parameters.environment) == 0:
        # Build and add the Other Environments response, if the original query did not include any
        pass

    if len(requested_parameters.heroes) == 1:
        # If only one Hero in the original query, build other Hero statistics for With this hero
        pass

    if len(requested_parameters.villains) == 1:
        # If Team Villain game, and if only one villain in original query, include With stats for other Team Villains
        pass

    # temp
    stats = models.Statistics(TotalGames=total_games, TotalWins=total_wins)

    return models.StatisticsResponse(RequestedSet=requested_parameters, OriginalRequestedPath=request.path, Statistics=stats)


def build_related_hero_stats(collection, original_hero: str = None) -> Dict[str, GameDetail]:
    """
    Collects all the other heroes in the response and builds a dictionary of "Hero Name": Statistics
    """
    heroes = get_all_heroes_in_results(collection)

    all_other_hero_stats = {}
    for hero in heroes:
        if hero == original_hero:
            continue
        individual_hero_collection = collection.where(lambda x: _is_hero(x, hero))
        incapped_games = individual_hero_collection.where(lambda x: _is_hero_incapped(x, hero))

        all_other_hero_stats[hero] = models.HeroStatistics(
            TotalGames=individual_hero_collection.count(),
            TotalWins=individual_hero_collection.where(lambda x: _is_win_condition(x.end_result)).count(),
            Incapacitated=incapped_games.count(),
            TotalWinsWhileIncapacitated=incapped_games.where(lambda x: _is_win_condition(x.end_result)).count(),
        )

    return all_other_hero_stats


def describe_query_parameters(operations=List[Operation]) -> models.RequestedSet:
    """
    parses the operations to provide a response of all the parameters in
    an easy to access form
    """

    heroes, opponents, locations, username = parse_for_rds_names(operations)

    return models.RequestedSet(heroes=heroes, villains=opponents, environment=locations, user=username)


def _is_win_condition(end_result: str) -> bool:
    """
    LINQ helper function - returns if the end_result is a HeroWinCondition compatible enum value or not.
    """
    return any([end_result == (win_condition.value if isinstance(end_result, str) else win_condition) for win_condition in HeroWinCondition])


def _is_hero(details: GameDetail, hero_name: str) -> bool:
    """
    LINQ helper function - returns if the given row (GameDetail) contains a given hero name in any position
    """
    return hero_name in [details.hero_one, details.hero_two, details.hero_three, details.hero_four, details.hero_five]


def _is_hero_incapped(details: GameDetail, hero_name: str) -> bool:
    """
    LINQ helper function - returns if the given row (GameDetail) contains a given hero name who was incapped in any position
    """
    comparison_pairs = [
        (details.hero_one, details.hero_one_incapped),
        (details.hero_two, details.hero_two_incapped),
        (details.hero_three, details.hero_three_incapped),
        (details.hero_four, details.hero_four_incapped),
        (details.hero_five, details.hero_five_incapped),
    ]
    return any(hero_name == comparison[0] and comparison[1] for comparison in comparison_pairs)


def get_all_heroes_in_results(results: Enumerable) -> list:
    """
    Parses the result for all the hero names and returns a sorted set of them
    """

    hero_one = results.distinct(lambda x: x.hero_one).to_list()
    hero_two = results.distinct(lambda x: x.hero_two).to_list()
    hero_three = results.distinct(lambda x: x.hero_three).to_list()
    hero_four = results.distinct(lambda x: x.hero_four).to_list()
    hero_five = results.distinct(lambda x: x.hero_five).to_list()

    all_heroes = [*hero_one, *hero_two, *hero_three, *hero_four, *hero_five]

    return sorted(set(all_heroes))
