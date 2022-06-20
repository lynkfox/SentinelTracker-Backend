from enum import Enum
from common.models.enums import EnhancedEnum


class SqlTables(EnhancedEnum):
    STATISTICS_DB_NAME = "sentinel_statistics"

    # table names
    ENVIRONMENTS = "environments"
    HEROES = "heroes"
    VILLAINS = "villains"
    USERS = "users"
    GAME_DETAILS = "gameDetails"
    HERO_TEAMS = "heroTeams"
    OPPONENTS = "opponents"
    OBLIVAEON_SETUPS = "oblivaeonSetups"


class SqlColumns(EnhancedEnum):
    ID = "id"
    ID_HASH = "id_hash"
    NON_POSITIONAL_HASH = "non_positional_hash"
    FULL_NAME = "full_name"
    BASE = "base"
    QUERY_NAME = "query_name_value"
    QUERY_ALT = "query_alt_value"
    ENTITY_TYPE = "entity_type"
    USERNAME = "username"
    HERO_ONE = "hero_one"
    HERO_TWO = "hero_two"
    HERO_THREE = "hero_three"
    HERO_FOUR = "hero_four"
    HERO_FIVE = "hero_five"
    VILLAIN_ONE = "villain_one"
    VILLAIN_TWO = "villain_two"
    VILLAIN_THREE = "villain_three"
    VILLAIN_FOUR = "villain_four"
    VILLAIN_FIVE = "villain_five"
    SCIONS = "scions"
    SHIELD = "shield"
    REWARDS = "rewards"
    ENTER_DATE = "entered_on"
    GAME_MODE = "game_mode"
    SELECTION_METHOD = "selection_method"
    PLATFORM = "platform"
    END_RESULT = "end_result"
    ESTIMATED_TIME = "estimated_time"
    HOUSE_RULES = "house_rules"
    NUMBER_OF_PLAYERS = "number_of_players"
    NUMBER_OF_HEROES = "number_of_heroes"
    PERCEIVED_DIFFICULTY = "perceived_difficulty"
    ROUNDS = "rounds"
    OBLIVAEON_DETAIL = "oblivaeon_details"
    HERO_TEAM = "hero_team"
    ENVIRONMENT = "environment"
    VILLAIN = "villain"
    H1_INCAP = "hero_one_incapped"
    H2_INCAP = "hero_two_incapped"
    H3_INCAP = "hero_three_incapped"
    H4_INCAP = "hero_four_incapped"
    H5_INCAP = "hero_five_incapped"
    V1_INCAP = "villain_one_incapped"
    V2_INCAP = "villain_two_incapped"
    V3_INCAP = "villain_three_incapped"
    V4_INCAP = "villain_four_incapped"
    V5_INCAP = "villain_five_incapped"
    ENTRY_IS_VALID = "entry_is_valid"
    VALID_TEAM = "valid_team"
    COMMENTS = "comments"
    ADVANCED = "advanced"
    CHALLENGE = "challenge"


HERO_TEAMS_COLUMNS = [
    SqlColumns.HERO_ONE.value,
    SqlColumns.HERO_TWO.value,
    SqlColumns.HERO_THREE.value,
    SqlColumns.HERO_FOUR.value,
    SqlColumns.HERO_FIVE.value,
    SqlColumns.VALID_TEAM.value,
    SqlColumns.ID_HASH.value,
]

OPPONENTS_COLUMNS = [
    SqlColumns.VILLAIN_ONE.value,
    SqlColumns.VILLAIN_TWO.value,
    SqlColumns.VILLAIN_THREE.value,
    SqlColumns.VILLAIN_FOUR.value,
    SqlColumns.VILLAIN_FIVE.value,
    SqlColumns.VALID_TEAM.value,
    SqlColumns.ID_HASH.value,
]

GAME_DETAILS_COLUMNS = [
    SqlColumns.USERNAME.value,
    SqlColumns.ENTER_DATE.value,
    SqlColumns.GAME_MODE.value,
    SqlColumns.SELECTION_METHOD.value,
    SqlColumns.PLATFORM.value,
    SqlColumns.END_RESULT.value,
    SqlColumns.ESTIMATED_TIME.value,
    SqlColumns.HOUSE_RULES.value,
    SqlColumns.NUMBER_OF_PLAYERS.value,
    SqlColumns.NUMBER_OF_HEROES.value,
    SqlColumns.PERCEIVED_DIFFICULTY.value,
    SqlColumns.ROUNDS.value,
    SqlColumns.OBLIVAEON_DETAIL.value,
    SqlColumns.HERO_TEAM.value,
    SqlColumns.ENVIRONMENT.value,
    SqlColumns.VILLAIN.value,
    SqlColumns.HERO_ONE.value,
    SqlColumns.H1_INCAP.value,
    SqlColumns.HERO_TWO.value,
    SqlColumns.H2_INCAP.value,
    SqlColumns.HERO_THREE.value,
    SqlColumns.H3_INCAP.value,
    SqlColumns.HERO_FOUR.value,
    SqlColumns.H4_INCAP.value,
    SqlColumns.HERO_FIVE.value,
    SqlColumns.H5_INCAP.value,
    SqlColumns.VILLAIN_ONE.value,
    SqlColumns.V1_INCAP.value,
    SqlColumns.VILLAIN_TWO.value,
    SqlColumns.V2_INCAP.value,
    SqlColumns.VILLAIN_THREE.value,
    SqlColumns.V3_INCAP.value,
    SqlColumns.VILLAIN_FOUR.value,
    SqlColumns.V4_INCAP.value,
    SqlColumns.VILLAIN_FIVE.value,
    SqlColumns.V5_INCAP.value,
    SqlColumns.ADVANCED.value,
    SqlColumns.CHALLENGE.value,
    SqlColumns.COMMENTS.value,
    SqlColumns.ENTRY_IS_VALID.value,
]
