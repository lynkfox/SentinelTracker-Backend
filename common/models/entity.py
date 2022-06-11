from dataclasses import dataclass, field
from typing import Optional
from common.models.enums import BoxSet, Type, ApiEventTypes
from common.models import Schema


@dataclass
class ApiEvent:
    event: {}
    path_parts: list = field(init=False)
    IS_OPTIONS: bool = field(init=False)
    IS_GET: bool = field(init=False)
    IS_POST: bool = field(init=False)

    def __post_init__(self):
        self.path_parts = (
            self.event.get("pathParameters", {}).get("proxy", "").split("/")
        )
        self.determine_type()

    def determine_type(self):
        """
        determines the type of the api call
        """

        self.method = self.event.get("httpMethod")

        self.IS_GET = self.method == ApiEventTypes.GET
        self.IS_OPTIONS = self.method == ApiEventTypes.CORS_PREFLIGHT
        self.IS_POST = self.method == ApiEventTypes.POST


@dataclass
class GetEntity(ApiEvent):
    entity_name: str = field(init=False)
    api_type: str = field(init=False)

    def __post_init__(self):
        self._is_allowed_method()

    def _is_allowed_method(self):
        """
        GetEntity only allowes Options and Get method calls.
        """
        if self.IS_OPTIONS:
            self.api_type = ApiEventTypes.CORS_PREFLIGHT

        elif self.IS_GET:
            self.api_type = ApiEventTypes.GET

        else:
            raise TypeError("Not a valid Type for GetEntity - must be GET or OPTIONS")
