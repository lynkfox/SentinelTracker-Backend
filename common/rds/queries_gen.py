from common.models.enums import Type
from common.sql_attributes import SqlTables
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ColumnGroup:
    """
    Common groupings of columns. Provided as Class Methods for organizational purposes
    """

    @classmethod
    def team_member(
        cls,
        prefix: Type = Type.HERO,
        table_name: SqlTables = SqlTables.GAME_DETAILS,
    ):
        """
        shortcut for the same column names used over and over again.
        """

        return ", ".join(cls.team_columns(prefix, table_name))

    @classmethod
    def team_columns(
        cls, prefix: Type = Type.HERO, table_name: SqlTables = SqlTables.GAME_DETAILS
    ) -> list:
        """
        returns a list of columns in order all prefixed, for use in only needing a few of them for positional lookups
        """
        cls._is_hero_or_villain(prefix)
        cls._is_hero_or_villain_team_table(table_name)

        suffixes = ["_one", "_two", "_three", "_four", "_five"]

        column_prefix = f"{table_name}.{prefix.value.lower()}"

        return [column_prefix + suffix for suffix in suffixes]

    @classmethod
    def _is_hero_or_villain(cls, prefix: Type):
        """
        Error Handling for hero_[number] column names.
        """
        if prefix is not Type.HERO and prefix is not Type.VILLAIN:
            raise ValueError("type Mismatch: must be HERO or VILLAIN")

    @classmethod
    def _is_hero_or_villain_team_table(cls, table_name: SqlTables):
        if (
            table_name is not SqlTables.HERO_TEAMS
            and table_name is not SqlTables.GAME_DETAILS
            and table_name is not SqlTables.OPPONENTS
        ):
            raise ValueError(
                "Table Mismatch: table_name must be GAME_DETAILS, HERO_TEAMS, or OPPONENTS"
            )


def character_is(
    character_name: str,
    prefix: Type = Type.HERO,
    table_name: SqlTables = SqlTables.GAME_DETAILS,
) -> str:
    """
    For Where clause of any sql query to find a character name in all the team names

    Parameters:
        character_name (str) : The fully put together name - use common.rds.character_full_name() to create it
        type (common.enums.Type): the type, Type.HERO or Type.VILLAIN
        table_name (common.sql_attributes.SqlTables): the table to pull these columns from. SqlTables.GAME_DETAILS, SqlTables.HERO_TEAMS, SqlTables.OPPONENTS

    """
    return f"`{character_name}` IN ({ColumnGroup.team_member(prefix, table_name)})"


def with_allies(names: List[str], prefix: Type = Type.HERO, positional=False) -> str:
    """
    using character_is and a list of up to 5 names builds a team query string

    Parameters:
        names (List[str]): common.rds.character_full_name() for each  character name. If positional is True, then the order will be respected.
        prefix (common.enums.Type): the type, Type.HERO or Type.VILLAIN
        positional (bool): (default: false) if True, maintains the same order of names and atomically sets the table as GAME_DETAILS,
            otherwise alphabetizes the list and sets table to HERO_TEAMS or OPPONENTS depending on Type
    """

    if not positional:
        names.sort()
        table_name = (
            SqlTables.HERO_TEAMS if prefix is Type.HERO else SqlTables.OPPONENTS
        )

    else:
        table_name = SqlTables.GAME_DETAILS

    columns = ColumnGroup.team_columns(prefix, table_name)[: len(names)]

    if len(names) == 1:
        return f"{columns[0]}=`{names[0]}`"

    return ", ".join([f"{value}=`{names[i]}`" for i, value in enumerate(columns)])
