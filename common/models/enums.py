from enum import Enum


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
    WAGER_MASTER  = "Mini: Wager Master"
    CHOKEPOINT = "Mini: Chokepoint"
    FINAL_WASTELAND = "Mini: The Final Wasteland"
    SILVER_GULCH = "Mini: Silver Gulch 1883"
    OMNITRON_IV = "Mini: Omnitron-IV"
    CELESTIAL_TRIBUNAL = "Mini: The Celestial Tribunal"


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
