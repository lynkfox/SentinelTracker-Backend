from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class ResourceNames:
    ITEM_DYNAMODB: ClassVar[str] = field(init=False, default="statistics-cache")
    STATISTICS_RDS: ClassVar[str] = field(init=False, default="statistics-rds")
    BACKEND_API: ClassVar[str] = field(init=False, default="SentinelTrackerAPI")
    STATISTICS: ClassVar[str] = field(init=False, default="Get-Sentinels-Statistics")
    POST_ENTRY: ClassVar[str] = field(init=False, default="Add-Entry-To-RDS")
    USER: ClassVar[str] = field(init=False, default="Get-Sentinels-Statistics-User")
    COMMON_LAYER: ClassVar[str] = field(init=False, default="common")


@dataclass(frozen=True)
class DirectoryLocations:
    FRONT_END: ClassVar[str] = field(init=False, default="front_end")
    STATISTICS: ClassVar[str] = field(init=False, default="lambda_functions/statistics")
    POST_ENTRY: ClassVar[str] = field(init=False, default="lambda_functions/game_detail_entry")
    COMMON_LAYER: ClassVar[str] = field(init=False, default="common.zip")


@dataclass(frozen=True)
class Environment:
    DEMO: ClassVar[str] = field(init=False, default="DEMO")
    DEV: ClassVar[str] = field(init=False, default="DEV")
    PROD: ClassVar[str] = field(init=False, default="PROD")
