from dataclasses import dataclass, field
from common._snippets import *


class Schema:
    event: dict

    def schema(self) -> dict:

        attributes = {
            attribute: value
            for attribute, value in self.__dict__.items()
            if not attribute.begins_with("_")
        }

        return _generate_schema(attributes)


def _generate_schema(values: dict) -> dict:
    return {}
