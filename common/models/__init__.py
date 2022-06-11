from dataclasses import dataclass, field
from common._snippets import *


@dataclass
class Schema:
    event: dict
    schema: dict = field(init=False)

    def _set_schema(self):
        attributes = {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not _ignored_attribute(attribute, value) or attribute == "event"
        }

        self.schema = _generate_schema(attributes)


def _generate_schema(values: dict) -> dict:
    """
    generates a Json Schema
    """

    for key, value in values.items():
        if type(value).__name__ in [
            String.__name__,
            Integer.__name__,
            Number.__name__,
            Null.__name__,
            Array.__name__,
        ]:
            snippet = value.schema
