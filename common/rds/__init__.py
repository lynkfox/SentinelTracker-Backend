from dis import dis
from re import L
from common.models.character_enums import (
    Character,
    AlternateTags,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)
import boto3
import json
from common.sql_attributes import SqlTables
import mysql.connector
import os

from dataclasses import dataclass, field
from common.attributes import DynamoAttributes
from common.models.enums import Selector, Comparator, Default, Type
from common.models.character_enums import Hero, Villain, Location, AlternateTags
from typing import Union, List, Tuple
from enum import Enum
from aws_lambda_powertools import Logger
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

logger = Logger(child=True)
CLIENT = boto3.client("secretsmanager")


def get_mysql_client():

    try:
        response = CLIENT.get_secret_value(SecretId=os.getenv("SECRET_NAME"))
    except ClientError as e:
        logger.exception("Client Error")
        raise e

    try:
        secrets = json.loads(response["SecretString"])

        return mysql.connector.connect(
            host=secrets["host"],
            user=secrets["username"],
            password=secrets["password"],
            database=SqlTables.STATISTICS_DB_NAME.value,
        )
    except Exception as e:
        logger.exception("unable to open sql connection")
        raise e


def character_full_name(
    full_name: Union[Character, str],
    alternate_name: Union[AlternateTags, str, None],
    mapping: dict,
) -> str:
    """
    Builds the "full_name" for a given Hero, Villain, or Environment entry in the RDS
    """
    alternate_name = ALTERNATE_TAG_DISPLAY_MAPPING.get(alternate_name)
    full_name = mapping.get(full_name)
    if alternate_name is not None:
        full_name = f"{full_name}{alternate_name}"

    return full_name


@dataclass
class Operation:
    instruction: Union[Selector, Comparator]
    entity_type: Type
    name_selection: Union[str, Default]
    alternate_selection: Union[str, Default]
    definitive: bool = field(default=False)


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
        self.path = self.path[:-1] if self.path[-1] == "/" else self.path
        self.path_parts = self.path.split("/")
        self.total_parts = len(self.path_parts)
        self.parse_path()

    def parse_path(self):
        """
        Parses the path, assuming it starts after /selector/ with no / in
        index 0. Builds Operations for each set, to allow any combination
        of /with /versus /in.

        Respects values of only allowing 1 versus, 1 in, and 4 with's per
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
        self.hero_count += self._increment_to_maximum(operation.entity_type, Selector.HERO, self.hero_count, 5)
        self.villain_count += self._increment_to_maximum(operation.entity_type, Selector.OPPONENT, self.villain_count, 5)
        self.environment_count += self._increment_to_maximum(
            operation.entity_type,
            Selector.LOCATION,
            self.environment_count,
            1,
        )

    def _check_number_of_comparisons(self, operation):
        """
        Checks comparison operations (versus and in) if there is more than 1
        """
        self.versus_count += self._increment_to_maximum(operation.instruction, Comparator.VERSUS, self.versus_count, 1)
        self.in_count += self._increment_to_maximum(operation.instruction, Comparator.IN, self.in_count, 1)

    def _increment_to_maximum(self, left: Enum, right: Enum, current: int, max: int):
        """
        Checks two values (left and right) and if they are the same, returns
        1 to increment the value, unless it puts it above the maximum
        (inclusive). If max reached, raises Value Error
        """
        if left == right:
            if current >= max:
                raise ValueError(f"Cannot have more than {max} {left.value} in a single call")
            return 1
        return 0

    def _build_operation(self, current_index) -> Operation:
        """
        Builds an Operation to add to the instructions.
        """
        try:
            instruction = self._determine_instruction(self.path_parts[current_index])

            next_part = self.path_parts[current_index + 1] if self.total_parts > current_index + 1 else Default.ALL

            follow_up_part = self.path_parts[current_index + 2] if self.total_parts > current_index + 2 else None

            entity_type, character_enum = self._determine_entity_type(self.path_parts[current_index], next_part, instruction)

            if character_enum == "user":
                name_selection = next_part
            else:
                name_selection = character_enum(next_part) if next_part != Default.ALL else Default.ALL

            if follow_up_part is not None and "definitive_" in follow_up_part:
                definitive = True
                follow_up_part = follow_up_part.replace("definitive_", "")

            else:
                definitive = False

            if follow_up_part is not None and (not Selector.has_member(follow_up_part) and not Comparator.has_member(follow_up_part)):
                alternate_selection = AlternateTags(follow_up_part)
            else:
                alternate_selection = Default.BASE

            if name_selection is Default.ALL:
                alternate_selection = None

            if alternate_selection is AlternateTags.definitive:
                alternate_selection = Default.BASE
                definitive = True

            return Operation(
                instruction,
                entity_type,
                name_selection,
                alternate_selection,
                definitive,
            )

        except ValueError as e:
            logger.exception(
                "Unable to determine Operation",
                extra={
                    "current_index": current_index,
                    "current_point": self.path_parts[current_index],
                },
            )

            raise ValueError("Unable to determine Operation")

        except Exception as e:
            logger.exception(
                "Unknown Error",
                extra={
                    "current_index": current_index,
                    "current_point": self.path_parts[current_index],
                },
            )

            raise e

    def _determine_instruction(self, path_part) -> Comparator:
        """
        Sets the Instruction based on the current point in the path unless
            its the first, then it returns START
        """
        if len(self.operations) == 0:
            return Comparator.START
        else:
            return Comparator(path_part)

    def _determine_entity_type(self, path_part, next_part, current_instruction) -> Tuple[Selector, Enum]:
        """
        Sets the Entity_Type to the one passed if the first instruction,
            else checks the Enums for determining the type (and dealing)
            with special situations like Akash'Bhuta

        Also returns the Enum type that follows the Selector, for use in
            determining name_selection, alternate_selection
        """
        if len(self.operations) == 0:
            select = Selector(path_part)

            dispatch = {Selector.HERO: Hero, Selector.OPPONENT: Villain, Selector.LOCATION: Location}

            return select, dispatch.get(select, "user")

        elif next_part == Default.ALL or self._not_a_known_enum(next_part):

            if current_instruction == Comparator.WITH:
                previous_instruction = self.operations[-1].entity_type
                if previous_instruction == Selector.HERO:
                    return previous_instruction, None
                if previous_instruction == Selector.OPPONENT:
                    return previous_instruction, None

                return self._determine_entity_by_attached_part(next_part)

            if current_instruction == Comparator.VERSUS:
                first_instruction = self.operations[0].entity_type
                if first_instruction == Selector.HERO:
                    return Selector.OPPONENT, None
                if first_instruction == Selector.OPPONENT:
                    return Selector.HERO, None

            if current_instruction == Comparator.IN:
                return Selector.LOCATION, Location

            if current_instruction == Comparator.FROM:
                return Selector.USER, "user"
        else:
            select, enum_type = self._determine_entity_by_attached_part(next_part)
            if select is not None:
                return select, enum_type

        raise ValueError("Unable to determine call")

    def _determine_entity_by_attached_part(self, next_part) -> Tuple[Selector, Enum]:

        if Hero.has_member(next_part):
            return Selector.HERO, Hero

        if Villain.has_member(next_part):
            return Selector.OPPONENT, Villain

        if Location.has_member(next_part):
            return Selector.LOCATION, Location

        raise ValueError()

    def _not_a_known_enum(self, next_part) -> bool:
        return not Hero.has_member(next_part) and not Villain.has_member(next_part) and not Location.has_member(next_part)


def generate_sql(instructions: List[Operation]) -> any:
    """
    generates an SQL query string.
    """


def generate_query(instructions: List[Operation]) -> any:
    """
    Takes Instructions and parses out appropriate PK/SK
    """
    first_instruction = instructions[0]
    pk = f"{first_instruction.entity_type.value.upper()}#{first_instruction.name_selection.value}"
