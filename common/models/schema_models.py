from pydantic import BaseModel, Field
from common.models.enums import BoxSet, Type
from typing import Optional


class Entity(BaseModel):
    name: str = Field(...)
    set: Optional[BoxSet] = Field(None)
    type: Optional[Type] = Field(None)
    total_games: Optional[int] = Field(None)
    total_wins: Optional[int] = Field(None)
    _pk: str = Field("ENTITY#")
    _sk: str = Field("META#")
