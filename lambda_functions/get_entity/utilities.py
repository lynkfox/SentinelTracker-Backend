from dataclasses import dataclass, field
from common.models.enums import Selector, Comparator, Default, Type
from common.models.character_enums import Hero, Villain, Environment, AlternateTags
from typing import Union, List, Tuple
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

                self._check_number_of_characters(operation)
                self._check_number_of_comparisons(operation)

                self.operations.append(operation)

    def _check_number_of_characters(self, operation):
        """
        Checks entities to see if there are more than maximum amount
        (5 heroes, 5 villains, 1 environment)
        """
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

    def _check_number_of_comparisons(self, operation):
        """
        Checks comparsion operations (versus and in) if there is more than 1
        """
        self.versus_count += self._increment_to_maximum(
            operation.instruction, Comparator.VERSUS, self.versus_count, 1
        )
        self.in_count += self._increment_to_maximum(
            operation.instruction, Comparator.IN, self.in_count, 1
        )

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
        instruction = self._determine_instruction(self.path_parts[current_index])

        next_part = (
            self.path_parts[current_index + 1]
            if self.total_parts > current_index + 1
            else Default.ALL
        )

        follow_up_part = (
            self.path_parts[current_index + 2]
            if self.total_parts > current_index + 2
            else None
        )

        entity_type, character_enum = self._determine_entity_type(
            self.path_parts[current_index], next_part, instruction
        )

        name_selection = (
            character_enum(next_part) if next_part != Default.ALL else Default.ALL
        )

        if follow_up_part is not None and (
            not Selector.has_member(follow_up_part)
            and not Comparator.has_member(follow_up_part)
        ):
            alternate_selection = AlternateTags(follow_up_part)
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

    def _determine_entity_type(
        self, path_part, next_part, current_instruction
    ) -> Tuple[Selector, Enum]:
        """
        Sets the Entity_Type to the one passed if the first instruction,
            else checks the Enums for determining the type (and dealing)
            with special situations like Akash'Bhuta

        Also returns the Enum type that follows the Selector, for use in
            determing name_selection, alternate_selection
        """
        if len(self.operations) == 0:
            select = Selector(path_part)

            if select == Selector.HERO:
                return select, Hero
            if select == Selector.VILLAIN:
                return select, Villain
            if select == Selector.ENVIRONMENT:
                return select, Environment

        elif next_part == Default.ALL:
            first_instruction = self.operations[0].entity_type
            last_instruction = self.operations[-1].entity_type

            if current_instruction == Comparator.WITH:
                if last_instruction == Selector.HERO:
                    return last_instruction, None
                if last_instruction == Selector.VILLAIN:
                    return last_instruction, None

            if current_instruction == Comparator.VERSUS:
                if first_instruction == Selector.HERO:
                    return Selector.VILLAIN, None
                if first_instruction == Selector.VILLAIN:
                    return Selector.HERO, None

            if current_instruction == Comparator.IN:
                return Selector.ENVIRONMENT, Environment

        else:
            if next_part == Hero.akash_bhuta or next_part == Villain.akash_bhuta:
                return self._deal_with_duplicate_type(next_part)

            if Hero.has_member(next_part):
                return Selector.HERO, Hero

            if Villain.has_member(next_part):
                return Selector.VILLAIN, Villain

            if Environment.has_member(next_part):
                return Selector.ENVIRONMENT, Environment

    def _deal_with_duplicate_type(self, path_part) -> Tuple[Selector, Enum]:
        """
        dealing with Type for those who have the same name as another
            entity type (ie: akash_bhuta)
        """
        for operation in self.operations:
            if operation.entity_type == Selector.HERO:
                return Selector.VILLAIN, Villain
            elif operation.entity_type == Selector.VILLAIN:
                return Selector.HERO, Hero
            else:
                continue
