from dataclasses import dataclass, field
from common.models.enums import Selector, Comparator, Default, Type
from common.models.character_enums import Hero, Villain, Environment
from typing import Union, List


@dataclass
class Operation:
    instruction: Union[Selector, Comparator]
    entity_type: Type
    primary_name: Union[str, Default]
    alternate: Union[str, Default]


@dataclass
class LookUp:
    path: str
    operations: List[Operation] = field(init=False, default_factory=list)
    path_parts: list = field(init=False, default_factory=list)
    total_parts: int = field(init=False, default=0)

    def __post_init__(self):
        # remove first character "/" from the path property
        self.path = self.path[1:] if self.path[0] == "/" else self.path
        self.path_parts = self.path.split("/")
        self.total_parts = len(self.path_parts)
        self.parse_path()

    def parse_path(self):
        for index, path_part in enumerate(self.path_parts):
            if Selector.has_member(path_part) or Comparator.has_member(path_part):
                self.operations.append(self._build_operation(current_index=index))

    def _build_operation(self, current_index) -> Operation:

        next_part = (
            self.path_parts[current_index + 1]
            if self.total_parts > current_index + 1
            else Default.ALL
        )
        follow_up_part = (
            self.path_parts[current_index + 2]
            if self.total_parts > current_index + 2
            else Default.BASE
        )

        instruction = self._determine_instruction(self.path_parts[current_index])
        entity_type = self._determine_entity_type(self.path_parts[current_index])

        primary_name = next_part

        if not Selector.has_member(follow_up_part) and not Comparator.has_member(
            follow_up_part
        ):
            alternate = follow_up_part
        else:
            alternate = Default.BASE

        if next_part is Default.ALL:
            alternate = None

        return Operation(instruction, entity_type, primary_name, alternate)

    def _determine_instruction(self, path_part) -> Comparator:
        if len(self.operations) == 0:
            return Comparator.START
        else:
            return Comparator(path_part)

    def _determine_entity_type(self, path_part) -> Selector:
        if len(self.operations) == 0:
            return Selector(path_part)
        else:
            if path_part == Hero.akash_bhuta or path_part == Villain.akash_bhuta:
                return self._deal_with_akash()

            if Hero.has_member(path_part):
                return Selector.HERO

            if Villain.has_member(path_part):
                return Selector.VILLAIN

            if Environment.has_member(path_part):
                return Selector.ENVIRONMENT

    def _deal_with_akash(self):
        if len(self.operations) == 0:
            return Selector(self.path_parts[0])
        else:
            pass
