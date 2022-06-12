from dataclasses import dataclass, field
from common.models.entity import ApiEvent
from common.models.enums import ApiEventTypes
from utilities import LookUp


@dataclass
class Statistics(ApiEvent):
    entity_name: str = field(init=False)
    api_type: str = field(init=False)
    look_up_data: LookUp = field(init=False)

    def __post_init__(self):
        self._is_allowed_method()

        self.look_up_data = LookUp(self.path)

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