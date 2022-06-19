from __future__ import annotations
from pydantic import BaseModel, Field, PrivateAttr, validator
from pydantic.fields import ModelField
from common.models.enums import Type
from common.models.character_enums import Location, Hero, Villain
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
from typing import Optional, Union, Dict, Any
from datetime import datetime


class User(BaseModel):
    """
    Model of a row in the Users Table.
    """

    username: str

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["User"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)


class OblivAeonDetail(BaseModel):
    """
    Model of a row in t he OblivAeonDetails table
    """

    scions: str = Field(
        ..., description="The Display names all together as a single string separated by - Name A-Name B-Name-C"
    )  # scion ID values concatted into id#-id#-id#-id#
    shield: str = Field(...)
    environments: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    player_one_heroes: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    player_two_heroes: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    player_three_heroes: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    player_four_heroes: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    player_five_heroes: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    rewards: Optional[str] = Field(description="The Display names all together as a single string separated by - Name A-Name B-Name-C")
    id_hash: Optional[str]

    @validator("id_hash", always=True)
    def hash_team(cls, id_hash, values):
        if id_hash is None or id_hash == "":
            return hash("".join([v if v is not None else "-" for k, v in values.items() if k in ["scions", "shield"]]))
        return id_hash

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["OblivAeonDetail"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            del schema["properties"]["id_hash"]


class HeroTeam(BaseModel):
    """
    The Hero Team - IN ALPHABETICAL ORDER in order.
    """

    hero_one: str = Field(...)
    hero_two: str = Field(...)
    hero_three: str = Field(...)
    hero_four: Optional[str]
    hero_five: Optional[str]
    id_hash: Optional[str]
    valid_team: Optional[bool]

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["HeroTeam"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            del schema["properties"]["id_hash"]
            del schema["properties"]["valid_team"]

    @validator("hero_five", always=True)
    def collapse_team(cls, hero_five, values):
        if hero_five is not None and values["hero_four"] is None:
            values["hero_four"] = hero_five
            hero_five = None
        return hero_five

    @validator("id_hash", always=True)
    def hash_team_positions(cls, id_hash, values):

        if id_hash is None or id_hash == "":
            return hash("".join([v if v is not None else "-" for k, v in values.items() if "hero" in k]))
        return id_hash

    @validator("valid_team", always=True)
    def validate_team(cls, validation, values):
        # alphabetize heroes
        if validation is None:
            members = [value for key, value in values.items() if (key.startswith("hero")) and value is not None]
            sorted_members = sorted(members)
            total_members = len(members)

            values["hero_one"] = sorted_members[0]
            values["hero_two"] = sorted_members[1] if total_members > 1 else None
            values["hero_three"] = sorted_members[2] if total_members > 2 else None
            values["hero_four"] = sorted_members[3] if total_members > 3 else None
            values["hero_five"] = sorted_members[4] if total_members > 4 else None

            # if there are duplications
            if len(set(members)) != len(members):
                return False

        else:
            return validation

        return True


class VillainOpponent(BaseModel):
    """
    Villain Team. This team should be entered ALPHABETICALLY
    """

    villain_one: str = Field(...)
    villain_two: Optional[str]
    villain_three: Optional[str]
    villain_four: Optional[str]
    villain_five: Optional[str]
    id_hash: Optional[str]
    valid_team: Optional[str]

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["VillainOpponent"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            del schema["properties"]["id_hash"]
            del schema["properties"]["valid_team"]

    @validator("villain_two", "villain_three", "villain_four", "villain_five", always=True)
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
    def hash_team_positions(cls, id_hash, values):
        if id_hash is None or id_hash == "":
            return hash("".join([str(v) if v is not None else "-" for k, v in values.items() if k != "id_hash"]))
        return id_hash

    @validator("valid_team", always=True)
    def validate_team(cls, validation, values):

        if validation is None:
            # alphabetize heroes
            members = [value for key, value in values.items() if (key.startswith("villain")) and value is not None]
            sorted_members = sorted(members)
            total_members = len(members)

            values["villain_one"] = sorted_members[0]
            values["villain_two"] = sorted_members[1] if total_members > 1 else None
            values["villain_three"] = sorted_members[2] if total_members > 2 else None
            values["villain_four"] = sorted_members[3] if total_members > 3 else None
            values["villain_five"] = sorted_members[4] if total_members > 4 else None

            # if there are duplications
            if len(set(members)) != len(members):
                return False

        else:
            return validation

        return True


class GameDetail(BaseModel):
    """
    Model of a row in the Game Details table
    """

    username: Union[User, str]
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
    hero_team: Union[HeroTeam, int]
    environment: str
    villain: Union[VillainOpponent, int]
    hero_one: Optional[str]
    hero_one_incapped: Optional[bool]
    hero_two: Optional[str]
    hero_two_incapped: Optional[bool]
    hero_three: Optional[str]
    hero_three_incapped: Optional[bool]
    hero_four: Optional[str]
    hero_four_incapped: Optional[bool]
    hero_five: Optional[str]
    hero_five_incapped: Optional[bool]
    villain_one: Optional[str]
    villain_one_incapped: Optional[bool]
    villain_two: Optional[str]
    villain_two_incapped: Optional[bool]
    villain_three: Optional[str]
    villain_three_incapped: Optional[bool]
    villain_four: Optional[str]
    villain_four_incapped: Optional[bool]
    villain_five: Optional[str]
    villain_five_incapped: Optional[bool]
    advanced: Optional[bool]
    challenge: Optional[bool]
    comment: Optional[str]
    entry_is_valid: bool = Field(True)

    class Config:
        use_enum_values = True
        anystr_strip_whitespace = True

        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type["GameDetail"]) -> None:
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)

            del schema["properties"]
            del schema["properties"]["entry_is_valid"]

    @validator("villain", always=True)
    def update_game_type(cls, opponent: VillainOpponent, values):
        if isinstance(opponent, int):
            return opponent
        if opponent.villain_two is not None:
            values["game_mode"] = GameMode.VILLAINS.value
        return opponent

    @validator("entry_is_valid", always=True)
    def validate_entry(cls, entry, values):
        """
        For inputting data from the google sheet, this value will determine if the google sheet value constitutes
        a valid game entry or not. If it doesn't, it simply marks this field as false in order to preserve the
        game entries but not include them in statistics.

        Coming from the database, this value is defaulted to true, so will always be there and the rest of the
        validation can be ignored.
        """
        if entry is not None:
            return entry

        # make sure if a team game that the number of villains is not more than the number of heroes
        villains = [v for k, v in values["villain"].__dict__.items() if ("villain" in k and "incapped" not in k) and v is not None]
        if len(villains) != 1 and len(villains) != values["number_of_heroes"]:
            return False

        # validate that the heroes are all unique
        if not values["hero_team"].valid_team:
            return False

        incapped_heroes = [v for k, v in values.items() if "hero" in k and "incapped" in k and v]

        # validate if all heroes are incapped that the end_result is not a Win condition.
        if len(incapped_heroes) == values["number_of_heroes"] and isinstance(values["end_result"], HeroWinCondition):
            return False

        # if either Challenge or Advanced is none that means this entry didnt have values (the length of the response
        # from google sheets wasn't long enough) which means this is an invalid entry.
        if values["challenge"] is None or values["advanced"] is None:
            return False

        return True
