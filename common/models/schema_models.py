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
    scions: str = Field(...)  # scion ID values concatted into id#-id#-id#-id#
    shield: str = Field(...)
    environments: Optional[str]  # id# concatted into id#-id#-id# ...
    player_one_heroes: Optional[str]  # id# concatted into id#-id#-id# ...
    player_two_heroes: Optional[str]  # id# concatted into id#-id#-id# ...
    player_three_heroes: Optional[str]  # id# concatted into id#-id#-id# ...
    player_four_heroes: Optional[str]  # id# concatted into id#-id#-id# ...
    player_five_heroes: Optional[str]  # id# concatted into id#-id#-id# ...
    rewards: Optional[str]  # reward ID values concatted into id#-id#-id#
    id_hash: Optional[str]

    @validator("id_hash", always=True)
    def hash_team(cls, id_hash, values):
        if id_hash is None or id_hash == "":
            return hash(
                "".join(
                    [
                        v if v is not None else "-"
                        for k, v in values.items()
                        if k != "id_hash"
                    ]
                )
            )
        return id_hash


class HeroTeam(BaseModel):
    hero_one: str = Field(...)
    hero_two: str = Field(...)
    hero_three: str = Field(...)
    hero_four: Optional[str]
    hero_five: Optional[str]
    id_hash: Optional[str]

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True

    @validator("hero_five", always=True)
    def collapse_team(cls, hero_five, values):
        if hero_five is not None and values["hero_four"] is None:
            values["hero_four"] = hero_five
            hero_five = None
        return hero_five

    @validator("id_hash", always=True)
    def hash_team(cls, id_hash, values):
        if id_hash is None or id_hash == "":
            return hash(
                "".join(
                    [
                        v if v is not None else "-"
                        for k, v in values.items()
                        if k != "id_hash"
                    ]
                )
            )
        return id_hash


class VillainOpponent(BaseModel):
    villain_one: str = Field(...)
    villain_two: Optional[str]
    villain_three: Optional[str]
    villain_four: Optional[str]
    villain_five: Optional[str]
    advanced: bool
    challenge: bool
    id_hash: Optional[str]

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True

    @validator(
        "villain_two", "villain_three", "villain_four", "villain_five", always=True
    )
    def collapse_team(cls, villain, values):
        """
        takes advantage of the fact that in validation on pydantic, values is only going to contain the attributes
        that are listed ahead of it (ie: the above order!) so with villain_four, values will only include
        villain_one, villain_two, villain_three.
        """
        latest_key = [key for key in values.keys()][-1]
        if villain is not None and values[latest_key] is None:
            values[latest_key] = villain
            return None
        return villain

    @validator("id_hash", always=True)
    def hash_team(cls, id_hash, values):
        if id_hash is None or id_hash == "":
            return hash(
                "".join(
                    [
                        str(v) if v is not None else "-"
                        for k, v in values.items()
                        if k != "id_hash"
                    ]
                )
            )
        return id_hash


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
    comment: Optional[str]

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True
