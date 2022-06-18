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
    TotalWins: int = Field(description="Total wins recorded with this RequestedSet", default=0)
    WinRate: float = Field(description="Derived: Win percentage", default=0.0)
    TotalLosses: int = Field(description="Derived: Number of losses", default=0)
    LossRate: float = Field(description="Derived: Loss percentage", default=0.0)

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["Statistics"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

    @validator("WinRate", always=True, allow_reuse=True)
    def calculate_win_rate(cls, wins, values):
        try:
            return round(values["TotalWins"] / values["TotalGames"], 2)
        except Exception:
            return 0.0

    @validator("TotalLosses", always=True, allow_reuse=True)
    def calculate_losses(cls, losses, values):
        try:
            return values["TotalGames"] - values["TotalWins"]
        except Exception:
            return 0

    @validator("LossRate", always=True, allow_reuse=True)
    def calculate_loss_rate(cls, losses, values):
        try:
            return round(values["TotalLosses"] / values["TotalGames"], 2)
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
    TotalWinsWhileIncapacitated: Optional[float] = Field(description="Total wins when incapacitated", default=0)
    WinRateWhenIncapacitated: Optional[float] = Field(description="Derived: Win rate when incapacitated", default=0.0)
    Versus: Optional[List[OpponentStatistics]]
    With: Optional[List[HeroStatistics]]
    In: Optional[List[LocationStatistics]]
    SpecialEndConditions: Optional[List[SpecialStatistics]]

    @validator("IncapacitatedRate", always=True, allow_reuse=True)
    def calculate_incap_rate(cls, incap, values):
        try:
            return round(values["Incapacitated"] / values["TotalGames"], 2)
        except Exception:
            return 0.0

    @validator("WinRateWhenIncapacitated", always=True, allow_reuse=True)
    def calculate_wins_while_incap_rate(cls, incap, values):
        try:
            return round(values["TotalWinsWhileIncapacitated"] / values["Incapacitated"], 2)
        except Exception:
            return 0.0


class OpponentStatistics(Statistics):
    comment: str = Field(default="Wins in this object are total times Heroes/Players have triumphed over this villain")
    AdvancedModeTotalGames: int = Field(description="Total games with Advanced Mode", default=0)
    AdvancedModeWins: int = Field(description="Total Wins by players against this Villain with Advanced Mode", default=0)
    AdvancedModeWinRate: float = Field(description="Derived: Win percentage of Advanced Mode against this Villain", default=0.0)
    ChallengeModeTotalGames: int = Field(description="Total games with Challenge Mode", default=0)
    ChallengeModeWins: int = Field(description="Total Wins by players against this Villain with Challenge Mode", default=0)
    ChallengeModeWinRate: float = Field(description="Derived: Win percentage of Challenge Mode against this Villain", default=0.0)
    UltimateModeTotalGames: int = Field(description="Total games with Ultimate Mode", default=0)
    UltimateModeWins: int = Field(description="Total Wins by players against this Villain with Ultimate Mode", default=0)
    UltimateModeWinRate: float = Field(description="Derived: Win percentage of Ultimate Mode against this Villain", default=0.0)
    Versus: Optional[List[HeroStatistics]]
    With: Optional[List[OpponentStatistics]]
    In: Optional[List[LocationStatistics]]
    SpecialEndConditions: Optional[List["SpecialStatistics"]]

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["OpponentStatistics"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            values = deepcopy(schema.get("properties", {}))
            comment = values.pop("comment", None)

            schema["properties"] = {"comment": comment}
            schema["properties"] = {**schema["properties"], **values}

    @validator("AdvancedModeWinRate", always=True, allow_reuse=True)
    def calculate_advanced_win_rate(cls, wins, values):
        try:
            return round(values["AdvancedModeWins"] / values["AdvancedModeTotalGames"], 2)
        except Exception:
            return 0.0

    @validator("ChallengeModeWinRate", always=True, allow_reuse=True)
    def calculate_challenge_win_rate(cls, wins, values):
        try:
            return round(values["ChallengeModeWins"] / values["ChallengeModeTotalGames"], 2)
        except Exception:
            return 0.0

    @validator("UltimateModeWinRate", always=True, allow_reuse=True)
    def calculate_ultimate_win_rate(cls, wins, values):
        try:
            return round(values["UltimateModeWins"] / values["UltimateModeTotalGames"], 2)
        except Exception:
            return 0.0


class UserStatistics(Statistics):
    username: str
    Games: Optional[List[str]] = Field(description="Links to specific games for this user")


class StatisticsResponse(BaseModel):
    RequestedSet: RequestedSet
    OriginalRequestedPath: str = Field(description="Original instruction path for the RequestedSet as reference")
    Statistics: Union[HeroStatistics, OpponentStatistics, UserStatistics, Statistics, None]

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["StatisticsResponse"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)
