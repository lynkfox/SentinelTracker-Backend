from dataclasses import dataclass, field
from common.models.enums import Selector, Comparator, Default, Type
from common.models.character_enums import Hero, Villain, Environment
from typing import Union, List
from enum import Enum


@dataclass
class Operation:
    instruction: Union[Selector, Comparator]
    entity_type: Type
    name_selection: Union[str, Default]
    alternate_selection: Union[str, Default]


@dataclass
class LookUp:
    path: str
    operations: List[Operation] = field(init=False, default_factory=list)
    path_parts: list = field(init=False, default_factory=list)
    total_parts: int = field(init=False, default=0)
    hero_count: int = field(init=False, default=0)
    environment_count: int = field(init=False, default=0)
    villain_count: int = field(init=False, default=0)
    versus_count: int = field(init=False, default=0)
    in_count: int = field(init=False, default=0)

    def __post_init__(self):
        # remove first character "/" from the path property
        self.path = self.path[1:] if self.path[0] == "/" else self.path
        self.path_parts = self.path.split("/")
        self.total_parts = len(self.path_parts)
        self.parse_path()

    def parse_path(self):
        """
        Parses the path, assuming it starts after /selector/ with no / in
        index 0. Builds Operations for each set, to allow any combination
        of /with /versus /in.

        Respects values of only allowing 1 versus, 1 in, and 4 withs per
        hero or villain
        """

        for index, path_part in enumerate(self.path_parts):
            if Selector.has_member(path_part) or Comparator.has_member(path_part):
                operation = self._build_operation(current_index=index)

                self.hero_count += self._increment_to_maximum(
                    operation.entity_type, Selector.HERO, self.hero_count, 5
                )
                self.villain_count += self._increment_to_maximum(
                    operation.entity_type, Selector.VILLAIN, self.villain_count, 5
                )
                self.environment_count += self._increment_to_maximum(
                    operation.entity_type,
                    Selector.ENVIRONMENT,
                    self.environment_count,
                    1,
                )
                self.versus_count += self._increment_to_maximum(
                    operation.instruction, Comparator.VERSUS, self.versus_count, 1
                )
                self.in_count += self._increment_to_maximum(
                    operation.instruction, Comparator.IN, self.in_count, 1
                )

                self.operations.append(operation)

    def _increment_to_maximum(self, left: Enum, right: Enum, current: int, max: int):
        """
        Checks two values (left and right) and if they are the same, returns
        1 to increment the value, unless it puts it above the maxium
        (inculsive). If max reached, raises Value Error
        """
        if left == right:
            if current >= max:
                raise ValueError(
                    f"Cannot have more than {max} {left.value} in a single call"
                )
            return 1
        return 0

    def _build_operation(self, current_index) -> Operation:
        """
        Builds an Operation to add to the instructions.
        """

        follow_up_part = (
            self.path_parts[current_index + 2]
            if self.total_parts > current_index + 2
            else Default.BASE
        )

        instruction = self._determine_instruction(self.path_parts[current_index])
        entity_type = self._determine_entity_type(self.path_parts[current_index])
        name_selection = (
            self.path_parts[current_index + 1]
            if self.total_parts > current_index + 1
            else Default.ALL
        )

        if not Selector.has_member(follow_up_part) and not Comparator.has_member(
            follow_up_part
        ):
            alternate_selection = follow_up_part
        else:
            alternate_selection = Default.BASE

        if name_selection is Default.ALL:
            alternate_selection = None

        return Operation(instruction, entity_type, name_selection, alternate_selection)

    def _determine_instruction(self, path_part) -> Comparator:
        """
        Sets the Instruction based on the current point in the path unless
            its the first, then it returns START
        """
        if len(self.operations) == 0:
            return Comparator.START
        else:
            return Comparator(path_part)

    def _determine_entity_type(self, path_part) -> Selector:
        """
        Sets the Entity_Type to the one passed if the first instruction,
            else checks the Enums for determining the type (and dealing)
            with special situations like Akash'Bhuta
        """
        if len(self.operations) == 0:
            return Selector(path_part)
        else:
            if path_part == Hero.akash_bhuta or path_part == Villain.akash_bhuta:
                return self._deal_with_duplicate_type(path_part)

            if Hero.has_member(path_part):
                return Selector.HERO

            if Villain.has_member(path_part):
                return Selector.VILLAIN

            if Environment.has_member(path_part):
                return Selector.ENVIRONMENT

    def _deal_with_duplicate_type(self, path_part):
        """
        dealing with Type for those who have the same name as another
        entity type (ie: akash_bhuta)
        """
        for operation in self.operations:
            if operation.entity_type == Selector.HERO:
                return Selector.VILLAIN
            elif operation.entity_type == Selector.VILLAIN:
                return Selector.HERO
            else:
                continue
