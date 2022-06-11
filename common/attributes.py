from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class DynamoAttributes:
    PARTITION_KEY: ClassVar[str] = "pk"
    SORT_KEY: ClassVar[str] = "sk"
    TYPE: ClassVar[str] = "type"
