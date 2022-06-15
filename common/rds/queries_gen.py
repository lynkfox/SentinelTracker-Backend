from common.models.enums import Type
from common.sql_attributes import SqlTables
from dataclasses import dataclass


@dataclass(frozen=True)
class ColumnGroup:
    """
    Common groupings of columns. Provided as Class Methods for organizational purposes
    """

    @classmethod
    def team_members(
        cls, prefix: Type = Type.HERO, table_name: SqlTables = SqlTables.GAME_DETAILS
    ):
        """
        shortcut for the same column names used over and over again.
        """
        column_prefix = f"{table_name}.{prefix.value.lower()}"
        return f"{column_prefix}_one, {column_prefix}_two, {column_prefix}_three, {column_prefix}_four, {column_prefix}_five"


def character_is(
    character_name: str,
    prefix: Type = Type.HERO,
    table_name: SqlTables = SqlTables.GAME_DETAILS,
):
    """
    For Where clause of any sql query to find a character name in all the team names

    Parameters:
        character_name (str) : The fully put together name - use common.rds.character_full_name() to create it
        type (common.enums.Type): the type, Type.HERO or Type.VILLAIN
        table_name (common.sql_attributes.SqlTables): the table to pull these columns from. SqlTables.GAME_DETAILS, SqlTables.HERO_TEAMS, SqlTables.OPPONENTS

    """

    if prefix is not Type.HERO and prefix is not Type.VILLAIN:
        raise ValueError("type Mismatch: must be HERO or VILLAIN")

    if prefix == Type.HERO and (
        table_name is not SqlTables.GAME_DETAILS
        and table_name is not SqlTables.HERO_TEAMS
    ):
        raise ValueError(
            "Table Mismatch: type is HERO, table_name must be GAME_DETAILS or HERO_TEAMS"
        )

    if prefix == Type.VILLAIN and (
        table_name is not SqlTables.GAME_DETAILS
        and table_name is not SqlTables.OPPONENTS
    ):
        raise ValueError(
            "Table Mismatch: type is VILLAIN, table_name must be GAME_DETAILS or OPPONENTS"
        )

    return f'"{character_name}" IN ({ColumnGroup.team_members(prefix, table_name)})'
