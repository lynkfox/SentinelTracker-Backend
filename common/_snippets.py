from dataclasses import dataclass, field
from typing import Optional


@dataclass
class JsonSchema:
    type: str
    schema: dict = field(init=False)

    def _build_schema_object(self) -> dict:
        return {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not attribute.startswith("_") and value is not None
        }


@dataclass
class String(JsonSchema):
    type: str = field(default="string")
    minLength: Optional[int] = field(default=None)
    maxLength: Optional[int] = field(default=None)
    format: Optional[str] = field(default=None)
    pattern: Optional[str] = field(default=None)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Number(JsonSchema):
    type: str = field(default="number")
    min: Optional[int] = field(default=None)
    max: Optional[int] = field(default=None)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Integer(JsonSchema):
    type: str = field(default="integer")
    min: Optional[int] = field(default=None)
    max: Optional[int] = field(default=None)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Array(JsonSchema):
    type: str = field(default="array")
    items: list = field(default_factory=list)

    def __post_init__(self):
        self.schema = self._build_schema_object()

    def _build_schema_object(self) -> dict:
        self.items = [item.__name__.lower() for item in self.items]
        return {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not attribute.startswith("_") and value is not None
        }
