from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass, field
from common.models.entity import ApiEvent
from common.models.enums import ApiEventTypes
from common.rds import LookUp
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Union, Dict, Any, Type


@dataclass
class StatsIncoming:
    event: dict
    path: str = field(init=False)
    path_parts: list = field(init=False)
    IS_OPTIONS: bool = field(init=False)
    IS_GET: bool = field(init=False)
    IS_POST: bool = field(init=False)
    entity_name: str = field(init=False)
    api_type: str = field(init=False)
    look_up_data: LookUp = field(init=False)

    def __post_init__(self):
        self.path = self.event.get("pathParameters", {}).get("proxy", "")
        self.path_parts = self.path.split("/")
        self.determine_type()
        self._is_allowed_method()
        self.look_up_data = LookUp(self.path)

    def determine_type(self):
        """
        determines the type of the api call
        """

        self.method = self.event.get("httpMethod")

        self.IS_GET = self.method == ApiEventTypes.GET.value
        self.IS_OPTIONS = self.method == ApiEventTypes.CORS_PREFLIGHT.value
        self.IS_POST = self.method == ApiEventTypes.POST.value

    def _is_allowed_method(self):
        """
        GetEntity only allows Options and Get method calls.
        """
        if self.IS_OPTIONS:
            self.api_type = ApiEventTypes.CORS_PREFLIGHT

        elif self.IS_GET:
            self.api_type = ApiEventTypes.GET

        else:
            raise TypeError("Not a valid Type for GetEntity - must be GET or OPTIONS")


class RequestedSet(BaseModel):
    """
    Details about the requested data set, which heroes, villains, environments, and users were asked to be retrieved in combination
    """

    heroes: Optional[List[str]]
    villains: Optional[List[str]]
    environment: Optional[List[str]]
    user: Optional[str]

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["RequestedSet"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)


class Statistics(BaseModel):
    """
    Base statistics - Wins are always from the Hero/Players perspective
    """

    TotalGames: int = Field(description="Total games recorded with this RequestedSet", default=0)
    TotalPlayerVictories: int = Field(description="Total wins recorded with this RequestedSet", default=0)
    PlayerVictoryRate: float = Field(description="Derived: Win percentage", default=0.0)
    TotalPlayerDefeats: int = Field(description="Derived: Number of losses", default=0)
    PlayerDefeatRate: float = Field(description="Derived: Loss percentage", default=0.0)

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["Statistics"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

    @validator("PlayerVictoryRate", always=True, allow_reuse=True)
    def calculate_win_rate(cls, wins, values):
        try:
            return round(values["TotalPlayerVictories"] / values["TotalGames"] * 100, 3)
        except Exception:
            return 0.0

    @validator("TotalPlayerDefeats", always=True, allow_reuse=True)
    def calculate_losses(cls, losses, values):
        try:
            return values["TotalGames"] - values["TotalPlayerVictories"]
        except Exception:
            return 0

    @validator("PlayerDefeatRate", always=True, allow_reuse=True)
    def calculate_loss_rate(cls, losses, values):
        try:
            return round(values["TotalPlayerDefeats"] / values["TotalGames"] * 100, 3)
        except Exception:
            return 0.0


class LocationStatistics(Statistics):
    """
    Statistics for a given Environment the game is played IN with the requested Characters (included in any combination of Heroes or Villains that dont include an IN keyword)
    """

    In: str = Field(description="Environment being compared in")


class SpecialStatistics(Statistics):
    SpecialCondition: str = Field(
        description="Special conditions of this particular Character, such as the Terra-Lunar-Impulsion beam end game state for Baron Blade"
    )


class HeroStatistics(Statistics):
    Incapacitated: Optional[int] = Field(description="Total times incapacitated", default=0)
    IncapacitatedRate: Optional[float] = Field(description="Derived: Incapacitated percentage", default=0.0)
    TotalPlayerVictoriesWhileIncapacitated: Optional[float] = Field(description="Total wins when incapacitated", default=0)
    PlayerVictoryRateWhenIncapacitated: Optional[float] = Field(description="Derived: Win rate when incapacitated", default=0.0)
    Versus: Optional[Dict[str, OpponentStatistics]] = Field(default_factory=dict)
    With: Optional[Dict[str, HeroStatistics]] = Field(default_factory=dict)
    In: Optional[Dict[str, LocationStatistics]] = Field(default_factory=dict)
    SpecialEndConditions: Optional[Dict[str, SpecialStatistics]] = Field(default_factory=dict)

    @validator("IncapacitatedRate", always=True, allow_reuse=True)
    def calculate_incap_rate(cls, incap, values):
        try:
            return round(values["Incapacitated"] / values["TotalGames"] * 100, 3)
        except Exception:
            return 0.0

    @validator("PlayerVictoryRateWhenIncapacitated", always=True, allow_reuse=True)
    def calculate_wins_while_incap_rate(cls, incap, values):
        try:
            return round(values["TotalPlayerVictoriesWhileIncapacitated"] / values["Incapacitated"] * 100, 3)
        except Exception:
            return 0.0


class OpponentStatistics(Statistics):
    AdvancedModeTotalGames: int = Field(description="Total games with Advanced Mode", default=0)
    AdvancedModePlayerVictories: int = Field(description="Total Wins by players against this Villain with Advanced Mode", default=0)
    AdvancedModePlayerVictoryRate: float = Field(description="Derived: Win percentage of Advanced Mode against this Villain", default=0.0)
    ChallengeModeTotalGames: int = Field(description="Total games with Challenge Mode", default=0)
    ChallengeModePlayerVictories: int = Field(description="Total Wins by players against this Villain with Challenge Mode", default=0)
    ChallengeModePlayerVictoryRate: float = Field(description="Derived: Win percentage of Challenge Mode against this Villain", default=0.0)
    UltimateModeTotalGames: int = Field(description="Total games with Ultimate Mode", default=0)
    UltimateModePlayerVictories: int = Field(description="Total Wins by players against this Villain with Ultimate Mode", default=0)
    UltimateModePlayerVictoryRate: float = Field(description="Derived: Win percentage of Ultimate Mode against this Villain", default=0.0)
    Versus: Optional[Dict[str, HeroStatistics]] = Field(default_factory=dict)
    With: Optional[Dict[str, OpponentStatistics]] = Field(default_factory=dict)
    In: Optional[Dict[str, LocationStatistics]] = Field(default_factory=dict)
    SpecialEndConditions: Optional[Dict[str, SpecialStatistics]] = Field(default_factory=dict)

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type[OpponentStatistics]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            values = deepcopy(schema.get("properties", {}))
            comment = values.pop("comment", None)

            schema["properties"] = {"comment": comment}
            schema["properties"] = {**schema["properties"], **values}

    @validator("AdvancedModePlayerVictoryRate", always=True, allow_reuse=True)
    def calculate_advanced_win_rate(cls, wins, values):
        try:
            return round(values["AdvancedModePlayerVictories"] / values["AdvancedModeTotalGames"] * 100, 3)
        except Exception:
            return 0.0

    @validator("ChallengeModePlayerVictoryRate", always=True, allow_reuse=True)
    def calculate_challenge_win_rate(cls, wins, values):
        try:
            return round(values["ChallengeModePlayerVictories"] / values["ChallengeModeTotalGames"] * 100, 3)
        except Exception:
            return 0.0

    @validator("UltimateModePlayerVictoryRate", always=True, allow_reuse=True)
    def calculate_ultimate_win_rate(cls, wins, values):
        try:
            return round(values["UltimateModePlayerVictories"] / values["UltimateModeTotalGames"] * 100, 3)
        except Exception:
            return 0.0


class UserStatistics(Statistics):
    username: str
    Games: Optional[List[str]] = Field(description="Links to specific games for this user")


class StatisticsResponse(BaseModel):
    RequestedSet: RequestedSet
    OriginalRequestedPath: str = Field(description="Original instruction path for the RequestedSet as reference")
    Statistics: Union[Statistics, HeroStatistics, OpponentStatistics, UserStatistics, None]

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["StatisticsResponse"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)
