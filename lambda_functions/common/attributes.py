from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class DynamoAttributes:
    PARTITION_KEY: ClassVar[str] = "pk"
    SORT_KEY: ClassVar[str] = "sk"
    ENTITY_NAME: ClassVar[str] = "entityName"
    TYPE: ClassVar[str] = "type"


@dataclass(frozen=True)
class TransactionTypes:
    GET_ALL: ClassVar[str] = "GetAll"
