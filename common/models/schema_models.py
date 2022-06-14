from pydantic import BaseModel, Field, PrivateAttr, validator
from common.models.enums import Type
from common.models.character_enums import Environment, Hero, Villain
from common.models.game_details_enums import BoxSet
from common.models.game_details_enums import (
    HeroLossCondition,
    HeroWinCondition,
    SelectionMethod,
    GameMode,
    Platform,
    GameLength,
)
import json
from typing import Optional, Union
from datetime import datetime


class Entity(BaseModel):
    name: str = Field(...)
    set: Optional[BoxSet] = Field(
        ..., description="Box Set this version of the entity came from"
    )
    type: Optional[Type] = Field(..., dscription="Type of Entity")
    total_games: Optional[int] = Field(0, ge=0)
    total_wins: Optional[int] = Field(0, ge=0)
    _pk: str = PrivateAttr()
    _sk: str = PrivateAttr()
    _url: str = PrivateAttr()

    class Config:
        title = "An Entity"
        underscore_attrs_are_private = True
        description = "A singular Representative of an Entity, either a Hero, Villain, or Environment."

    def __init__(self, **data):
        super().__init__(**data)
        self._pk = self.name.upper().replace(" ", "_")
        self._sk = f"{self.type.name}#{self._pk}#META"
        self._url = f"/entity/{self.type.name.lower()}/{self.name}".replace(
            " ", "_"
        ).lower()


class EntityComparison(BaseModel):
    character: str = Field(...)
    compared_against: str = Field(...)
    total_games: Optional[int] = Field(0, ge=0)
    total_wins: Optional[int] = Field(0, ge=0)
    _pk: str = PrivateAttr()
    _sk: str = PrivateAttr()
    _url: str = PrivateAttr()


class User(BaseModel):
    user_id: str = Field(...)
    name: str = Field(...)
    total_games: Optional[int] = Field(0, ge=0)
    total_wins: Optional[int] = Field(0, ge=0)
    _pk: str = PrivateAttr()
    _sk: str = PrivateAttr()
    _url: str = PrivateAttr()

    class Config:
        title = "An Entity"
        underscore_attrs_are_private = True
        description = "A singular Representative of a User"

    def __init__(self, **data):
        super().__init__(**data)
        self._pk = f"{self.user_id}#USER"
        self._sk = f"#META"
        self._url = f"/user/{self.user_id}".replace(" ", "_").lower()


class Username(BaseModel):
    username: str
    dynamo_meta_query: Optional[str]
    total_wins: Optional[int]
    total_games: Optional[int]

    @validator("dynamo_meta_query", always=True)
    def create_dynamo_meta_query(cls, value, values):
        return json.dumps({"pk": f"{values['username']}#USER", "sk": f"#META"})


class OblivAeonDetail(BaseModel):
    scions: str = Field(...)
    shield: str = Field(...)
    rewards: Optional[str]
    id_hash: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)
        self.id_hash = (
            hash(f"{self.scions}{self.shield}{self.rewards}")
            if self.id_hash is None
            else self.id_hash
        )


class HeroTeam(BaseModel):
    hero_one: str = Field(...)
    hero_two: str = Field(...)
    hero_three: str = Field(...)
    hero_four: Optional[str]
    hero_five: Optional[str]
    id_hash: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)
        hero4 = self.hero_four if self.hero_four is not None else ""
        hero5 = self.hero_five if self.hero_five is not None else ""
        self.id_hash = (
            hash(f"{self.hero_one}{self.hero_two}{self.hero_three}{hero4}{hero5}")
            if self.id_hash is None
            else self.id_hash
        )


class VillainOpponent(BaseModel):
    villain_one: str = Field(...)
    villain_two: Optional[str]
    villain_three: Optional[str]
    villain_four: Optional[str]
    villain_five: Optional[str]
    id_hash: Optional[str]

    def __init__(self, **data):
        super().__init__(**data)
        villain4 = self.villain_four if self.villain_four is not None else ""
        villain5 = self.villain_five if self.villain_five is not None else ""
        self.id_hash = (
            hash(
                f"{self.villain_one}{self.villain_two}{self.villain_three}{villain4}{villain5}"
            )
            if self.id_hash is None
            else self.id_hash
        )


class GameDetail(BaseModel):
    username: Optional[Username]
    entered_on: datetime
    game_mode: Optional[GameMode]
    selection_method: Optional[SelectionMethod]
    platform: Optional[Platform]
    end_result: Union[HeroLossCondition, HeroWinCondition, None]
    estimated_time: Optional[GameLength]
    house_rules: Optional[str]
    number_of_players: Optional[int]
    number_of_heroes: Optional[int]
    perceived_difficulty: Optional[int]
    rounds: Optional[int] = Field()
    oblivaeon_details: Optional[OblivAeonDetail]
    hero_team: HeroTeam
    environment: str
    villain: VillainOpponent
    hero_one_incapped: Optional[bool] = Field(False)
    hero_two_incapped: Optional[bool] = Field(False)
    hero_three_incapped: Optional[bool] = Field(False)
    hero_four_incapped: Optional[bool]
    hero_five_incapped: Optional[bool]
    villain_one_incapped: Optional[bool] = Field(True)
    villain_two_incapped: Optional[bool]
    villain_three_incapped: Optional[bool]
    villain_four_incapped: Optional[bool]
    villain_five_incapped: Optional[bool]
