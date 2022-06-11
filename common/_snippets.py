from dataclasses import dataclass, field
from typing import Optional


def _ignored_attribute(attribute: str, value: any) -> bool:
    """
    Checks attribute and values to see if this should be ignored in the
    schema output.

    Returns:
        (bool): True -> ignore this attribute/value
    """
    if attribute.startswith("_"):
        return True

    if value is None:
        return True

    if (isinstance(value, list) or isinstance(value, dict)) and len(value) == 0:
        return True

    return False


@dataclass
class SchemaSnippet:
    type: str
    schema: dict = field(init=False)

    def _build_schema_object(self) -> dict:
        return {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not _ignored_attribute(attribute, value)
        }


@dataclass
class String(SchemaSnippet):
    type: str = field(default="string")
    minLength: Optional[int] = field(default=None)
    maxLength: Optional[int] = field(default=None)
    format: Optional[str] = field(default=None)
    pattern: Optional[str] = field(default=None)
    enum: Optional[list] = field(default_factory=list)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Number(SchemaSnippet):
    type: str = field(default="number")
    min: Optional[int] = field(default=None)
    max: Optional[int] = field(default=None)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Integer(SchemaSnippet):
    type: str = field(default="integer")
    min: Optional[int] = field(default=None)
    max: Optional[int] = field(default=None)

    def __post_init__(self):
        self.schema = self._build_schema_object()


@dataclass
class Array(SchemaSnippet):
    type: str = field(default="array")
    items: list = field(default_factory=list)

    def __post_init__(self):
        self.schema = self._build_schema_object()

    def _build_schema_object(self) -> dict:
        self.items = [item.__name__.lower() for item in self.items]
        return {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not _ignored_attribute(attribute, value)
        }


@dataclass
class Object(SchemaSnippet):
    type: str = field(default="object")
    properties: dict = field(default_factory=dict)
    required: list = field(default_factory=list)
    oneOf: dict = field(default_factory=dict)
