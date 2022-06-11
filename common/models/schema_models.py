from pydantic import BaseModel, Field, PrivateAttr
from pydantic.dataclasses import dataclass
from common.models.enums import BoxSet, Type
from typing import Optional


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
        description = "A singluar Representitive of an Entity, either a Hero, Villain, or Environment."

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


class Game(BaseModel):
    pass


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
        description = "A singluar Representitive of a User"

    def __init__(self, **data):
        super().__init__(**data)
        self._pk = self.user_id
        self._sk = f"USER#{self.name}#META"
        self._url = f"/user/{self.user_id}".replace(" ", "_").lower()
