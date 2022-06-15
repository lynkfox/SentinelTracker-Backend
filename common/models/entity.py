from dataclasses import dataclass, field
from typing import Optional
from common.models.enums import ApiEventTypes


@dataclass
class ApiEvent:
    event: dict
    path: str = field(init=False)
    path_parts: list = field(init=False)
    IS_OPTIONS: bool = field(init=False)
    IS_GET: bool = field(init=False)
    IS_POST: bool = field(init=False)

    def __post_init__(self):
        self.path = self.event.get("pathParameters", {}).get("proxy", "")
        self.path_parts = self.path.split("/")
        self.determine_type()

    def determine_type(self):
        """
        determines the type of the api call
        """

        self.method = self.event.get("httpMethod")

        self.IS_GET = self.method == ApiEventTypes.GET
        self.IS_OPTIONS = self.method == ApiEventTypes.CORS_PREFLIGHT
        self.IS_POST = self.method == ApiEventTypes.POST
