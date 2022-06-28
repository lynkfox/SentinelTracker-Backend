from __future__ import annotations
from dataclasses import dataclass, field
from common.models.enums import ApiEventTypes
from common.models.schema_models import GameDetail
import json
from typing import List, Optional, Union, Dict, Any, Type


@dataclass
class GameDetailIncoming:
    event: dict
    IS_OPTIONS: bool = field(init=False)
    IS_GET: bool = field(init=False)
    IS_POST: bool = field(init=False)
    entity_name: str = field(init=False)
    api_type: str = field(init=False)
    entry_data: Optional[GameDetail] = field(init=False)
    method: str = field(init=False)

    def __post_init__(self):
        self.method = self.event.get("httpMethod")
        self.determine_type()
        self._is_allowed_method()
        body = self.event.get("body")

        self.entry_data = GameDetail(**json.loads(body)) if body is not None else None

    def determine_type(self):
        """
        determines the type of the api call
        """

        self.IS_GET = self.method == ApiEventTypes.GET.value
        self.IS_OPTIONS = self.method == ApiEventTypes.CORS_PREFLIGHT.value
        self.IS_POST = self.method == ApiEventTypes.POST.value

    def _is_allowed_method(self):
        """
        GetEntity only allows Options and Get method calls.
        """
        if self.IS_OPTIONS:
            self.api_type = ApiEventTypes.CORS_PREFLIGHT

        elif self.IS_POST:
            self.api_type = ApiEventTypes.POST

        elif self.IS_GET:
            self.api_type = ApiEventTypes.GET

        else:
            raise TypeError("Not a valid Type for AddEntry")
