from py_linq import Enumerable
import os
import models
from common.rds import LookUp, Operation, character_full_name_to_enums
from common.rds.queries_gen import parse_for_rds_names
from common.models.schema_models import GameDetail
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition
from common.models.character_enums import HERO_DISPLAY_MAPPING, LOCATION_DISPLAY_MAPPING, VILLAIN_DISPLAY_MAPPING
from common.hardcoded_data.all_names import HERO_NAMES, VILLAIN_SINGLE_NAMES, LOCATION_NAMES, VILLAIN_TEAM_NAMES
from common.hardcoded_data.ignored_names import IGNORE_THESE
from typing import List, Dict


PRIMARY_ENDPOINT = os.getenv("ENDPOINT", "")


def calculate(request: LookUp, response: List[GameDetail]) -> models.StatisticsResponse:
    """
    Calculates the various statistics for a given request
    """

    # py-linq Enumerable, for using LINQ style syntax
    collection = Enumerable(response)

    requested_parameters = describe_query_parameters(request.operations)
    total_games = len(response)
    total_wins = collection.where(lambda x: _is_win_condition(x.end_result)).count()

    # default
    stats = models.Statistics(TotalGames=total_games, TotalPlayerVictories=total_wins)

    if (
        (requested_parameters.heroes is None or len(requested_parameters.heroes) == 0) and len(requested_parameters.villains) >= 1
    ) or request.path_parts[0] == "villain":
        stats = build_opponent_stats(request, collection, total_games, total_wins)

    if (
        requested_parameters.villains is None or len(requested_parameters.villains) == 0 and len(requested_parameters.heroes) >= 1
    ) or request.path_parts[0] == "hero":
        # Build Hero and Hero Team response:
        #   - includes: Hero/Team stats and against villains
        #   - mutual exclusive to the one above.

        stats = models.HeroStatistics(
            TotalGames=total_games,
            TotalPlayerVictories=total_wins,
            Versus=build_related_links([*VILLAIN_SINGLE_NAMES, *VILLAIN_TEAM_NAMES], VILLAIN_DISPLAY_MAPPING, "versus", f"{request.path}")
            if len(requested_parameters.villains) == 0
            else None,
        )

    if requested_parameters.environment is None or len(requested_parameters.environment) == 0:
        # Build and add the Other Environments response, if the original query did not include any
        stats.In = build_related_links(LOCATION_NAMES, LOCATION_DISPLAY_MAPPING, "in", f"{request.path}")

    if len(requested_parameters.heroes) == 1:
        # If only one Hero in the original query, build other Hero statistics for With this hero
        stats.With = build_related_links(
            HERO_NAMES, HERO_DISPLAY_MAPPING, "with", f"{request.path}", original_character=requested_parameters.heroes[0]
        )

        incapped_collection = collection.where(lambda x: _is_hero_incapped(x, requested_parameters.heroes[0]))
        stats.Incapacitated = incapped_collection.count()
        stats.TotalPlayerVictoriesWhileIncapacitated = incapped_collection.where(lambda x: _is_win_condition(x.end_result)).count()

    if len(requested_parameters.villains) >= 1 and requested_parameters.villains[0] in VILLAIN_TEAM_NAMES:
        # If Team Villain game, and if only one villain in original query, include With stats for other Team Villains
        stats.With = build_related_links(
            VILLAIN_TEAM_NAMES, VILLAIN_DISPLAY_MAPPING, "with", f"{request.path}", original_character=requested_parameters.villains[0]
        )

    return models.StatisticsResponse(RequestedSet=requested_parameters, OriginalRequestedPath=request.path, Statistics=stats)


def build_opponent_stats(request, collection, total_games, total_wins):
    """
    Build Solo Villain or Villain Team response:
        - includes: Villain stats, Against Other Heroes
        - mutually exclusive to the next function
    """

    advanced_games_collection = collection.where(lambda x: x.advanced is True)
    challenge_games_collection = collection.where(lambda x: x.challenge is True)
    ultimate_games_collection = challenge_games_collection.where(lambda x: x.advanced is True)

    return models.OpponentStatistics(
        TotalGames=total_games,
        TotalPlayerVictories=total_wins,
        AdvancedModeTotalGames=advanced_games_collection.count(),
        AdvancedModePlayerVictories=advanced_games_collection.where(lambda x: _is_win_condition(x.end_result)).count(),
        ChallengeModeTotalGames=challenge_games_collection.count(),
        ChallengeModePlayerVictories=challenge_games_collection.where(lambda x: _is_win_condition(x.end_result)).count(),
        UltimateModeTotalGames=ultimate_games_collection.count(),
        UltimateModePlayerVictories=ultimate_games_collection.where(lambda x: _is_win_condition(x.end_result)).count(),
        Versus=build_related_links(HERO_NAMES, HERO_DISPLAY_MAPPING, "versus", f"{request.path}"),
    )


def build_related_links(names: list, mapping: dict, type: str, prefix: str = None, original_character: str = None) -> Dict[str, GameDetail]:
    """
    Builds links to all heroes based on the mapping given and the prefix.
    """

    parts = prefix.split("/")
    versus = ""
    if "versus" in parts:
        index = parts.index("versus")
        prefix = "/".join(parts[:index])
        versus = "/".join(parts[index:])
        type = "" if type == "versus" else type

    all_reference_links = {}
    for name in names:
        if name in IGNORE_THESE or name == original_character:
            continue

        primary, alternate = character_full_name_to_enums(name, mapping)

        if primary is None:
            continue

        prepared_tags = [tag.value.replace("alt_", "") for tag in alternate if tag is not None]
        if len(prepared_tags) == 2:
            prepared_tags = f"/{prepared_tags[0]}_{prepared_tags[1]}"
        elif len(prepared_tags) > 0:
            prepared_tags = f"/{prepared_tags[0]}"
        else:
            prepared_tags = ""

        clean_value = f"{PRIMARY_ENDPOINT}/{prefix}/{type}/{primary.value}{prepared_tags}/{versus}".replace("//", "/")

        all_reference_links[name] = clean_value

    return all_reference_links


def is_hero_incapped(details: GameDetail, hero_name: str) -> bool:
    """
    Determines if the hero was incapped within this game.
    """
    dispatch_order = [
        (details.hero_one, details.hero_one_incapped),
        (details.hero_two, details.hero_two_incapped),
        (details.hero_three, details.hero_three_incapped),
        (details.hero_four, details.hero_four_incapped),
        (details.hero_five, details.hero_five_incapped),
    ]

    for check in dispatch_order:
        if check[0] == hero_name and check[1] is True:
            return True

    return False


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

    return sorted(
        set(results.select_many(lambda x: (x.hero_one, x.hero_two, x.hero_three, x.hero_four, x.hero_five)).except_(Enumerable([None])).to_list())
    )
