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
    VILLAINS = "Villians of the Multiverse"
    OBLIVAEON = "OblivAeon"


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
