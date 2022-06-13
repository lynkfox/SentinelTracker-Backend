from enum import Enum
from dataclasses import dataclass, field
from typing import ClassVar


class BoxSet(Enum):
    FIRST_EDITION = "First Edition"
    ENHANCED_EDITION = "Enhanced Edition"
    DEFINITIVE_EDITION = "Definitive Edition"
    ROOK_CITY = "Rook City"
    INFERNAL_RELICS = "Infernal Relics"
    SHATTERED_TIMELINES = "Shattered Timelines"
    VENGEANCE = "Vengeance"
    WRATH_OF_THE_COSMOS = "Wrath of the Cosmos"
    VILLAINS = "Villains of the Multiverse"
    OBLIVAEON = "OblivAeon"
    UNITY = "Mini: Unity"
    SCHOLAR = "Mini: Scholar"
    GUISE = "Mini: Guise"
    STUNTMAN = "Mini: Stuntman"
    BENCHMARK = "Mini: Benchmark"
    VOID_GUARD = "Mini: The Void Guard"
    AMBUSCADE = "Mini: Ambuscade"
    MISS_INFORMATION = "Mini: Miss Information"
    WAGER_MASTER = "Mini: Wager Master"
    CHOKEPOINT = "Mini: Chokepoint"
    FINAL_WASTELAND = "Mini: The Final Wasteland"
    SILVER_GULCH = "Mini: Silver Gulch 1883"
    OMNITRON_IV = "Mini: Omnitron-IV"
    CELESTIAL_TRIBUNAL = "Mini: The Celestial Tribunal"
    CAULDRON = "Cauldron"
    CAULDRON_EXPERIMENTAL = "Cauldron: Experimental"
    CAULDRON_STORMFALL = "Cauldron: Stormfall"
    CAULDRON_ADRIFT = "Cauldron: Adrift"


class Type(Enum):
    HERO = "Hero"
    VILLAIN = "Villain"
    TEAM_VILLAIN = "Team Villain"
    SCION = "Scion"
    ENVIRONMENT = "Environment"


class ApiEventTypes(Enum):
    CORS_PREFLIGHT = "OPTIONS"
    GET = "GET"
    POST = "POST"


class ApiEnum(Enum):
    @classmethod
    def has_member(cls, key) -> bool:
        """
        Quick check to see if key is within this class.
        """
        if isinstance(key, str):
            return key.upper() in cls.__members__
        elif isinstance(key, Enum):
            return key.name in cls.__members__
        else:
            return False


class Selector(ApiEnum):
    """
    Restful API selector types
    """

    VILLAIN = "villain"
    HERO = "hero"
    ENVIRONMENT = "environment"


class Comparator(ApiEnum):
    """
    Restful API comparator types
    """

    START = "start"
    VERSUS = "versus"
    WITH = "with"
    IN = "in"


class Default(Enum):
    """
    Defaults for entities in LookUp and elsewhere.
    """

    BASE = "base"
    ALL = "all"


@dataclass(frozen=True)
class SqlTables:
    STATISTICS_DB_NAME: ClassVar[str] = "sentinel_statistics"

    # table names
    BOX_SETS: ClassVar[str] = "boxSets"
    ENVIRONMENTS: ClassVar[str] = "environments"
    HEROES: ClassVar[str] = "heroes"
    VILLAINS: ClassVar[str] = "villains"
    USERS: ClassVar[str] = "users"
    GAME_DETAILS: ClassVar[str] = "gameDetails"
    HERO_TEAMS: ClassVar[str] = "heroTeams"
    OPPONENTS: ClassVar[str] = "opponents"
    OBLIVAEON_SETUPS: ClassVar[str] = "oblivaeonSetups"


class SqlColumns:
    ID = "id"
    ID_HASH = "id_hash"
    FULL_NAME = "full_name"
    BOX_SET = "box_set"
    DYNAMO_META = "dynamo_meta_query"
    TOTAL_WINS = "total_wins"
    TOTAL_GAMES = "total_games"
    NEMESIS = "nemesis"
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
    ENTER_DATE = "entered_on "
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
