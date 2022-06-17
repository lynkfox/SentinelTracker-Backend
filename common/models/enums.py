from enum import Enum
from dataclasses import dataclass, field
from typing import ClassVar

#####################################################
#
#   Api End Point Enums
#
#####################################################


class EnhancedEnum(Enum):
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value


class Type(Enum):
    HERO = "Hero"
    VILLAIN = "Villain"
    TEAM_VILLAIN = "Team Villain"
    SCION = "Scion"
    LOCATION = "Environment"
    USER = "User"


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
            return key.upper() in cls.__members__ or key.lower() in [x.value.lower() for x in cls.__members__.values()]
        elif isinstance(key, Enum):
            return key.name in cls.__members__
        else:
            return False


class Selector(ApiEnum):
    """
    Restful API selector types
    """

    OPPONENT = "villain"
    HERO = "hero"
    LOCATION = "environment"
    USER = "user"


class Comparator(ApiEnum):
    """
    Restful API comparator types
    """

    START = "start"
    VERSUS = "versus"
    WITH = "with"
    IN = "in"
    FROM = "from"


class Default(Enum):
    """
    Defaults for entities in LookUp and elsewhere.
    """

    BASE = "base"
    ALL = "all"
