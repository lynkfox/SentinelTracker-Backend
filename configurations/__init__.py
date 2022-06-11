from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class ResourceNames:
    ITEM_DYNAMODB: ClassVar[str] = field(init=False, default="statistics")
    BACKEND_API: ClassVar[str] = field(init=False, default="SentinelTrackerAPI")
    GET_ENTITY: ClassVar[str] = field(init=False, default="Get-Sentinels-Entities")
    COMMON_LAYER: ClassVar[str] = field(init=False, default="common")


@dataclass(frozen=True)
class DirectoryLocations:
    FRONT_END: ClassVar[str] = field(init=False, default="front_end")
    GET_ENTITY: ClassVar[str] = field(init=False, default="lambda_functions/get_entity")
    COMMON_LAYER: ClassVar[str] = field(init=False, default="common.zip")


@dataclass(frozen=True)
class Environment:
    DEMO: ClassVar[str] = field(init=False, default="DEMO")
    DEV: ClassVar[str] = field(init=False, default="DEV")
    PROD: ClassVar[str] = field(init=False, default="PROD")
