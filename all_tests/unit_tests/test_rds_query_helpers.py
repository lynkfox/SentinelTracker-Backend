from re import S
from common.rds.queries_gen import *
import pytest


class Test_character_is:
    def test_returns_str(self):
        assert isinstance(character_is("Test"), str)

    def test_raises_value_error_on_not_type_hero(self):
        with pytest.raises(
            ValueError, match="type Mismatch: must be HERO or VILLAIN"
        ) as e:
            character_is("test", Type.ENVIRONMENT)

    def test_raises_value_error_on_type_hero_but_not_hero_team_table(self):
        with pytest.raises(
            ValueError,
            match="Table Mismatch: type is HERO, table_name must be GAME_DETAILS or HERO_TEAMS",
        ) as e:
            character_is("test", Type.HERO, SqlTables.OPPONENTS)

    def test_raises_value_error_on_type_villain_but__not_opponent_table(self):
        with pytest.raises(
            ValueError,
            match="Table Mismatch: type is VILLAIN, table_name must be GAME_DETAILS or OPPONENTS",
        ) as e:
            character_is("test", Type.VILLAIN, SqlTables.HERO_TEAMS)

    def test_with_hero_prefix_column_names_correctly(self):
        test_response = character_is("Absolute Zero", Type.HERO)
        assert (
            test_response
            == '"Absolute Zero" IN (gameDetails.hero_one, gameDetails.hero_two, gameDetails.hero_three, gameDetails.hero_four, gameDetails.hero_five)'
        )

    def test_with_hero_and_hero_teams_table_prefix_column_names_correctly(self):
        test_response = character_is("Absolute Zero", Type.HERO, SqlTables.HERO_TEAMS)
        assert (
            test_response
            == '"Absolute Zero" IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)'
        )

    def test_with_villain_and_no_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN)
        assert (
            test_response
            == '"Baron Blade" IN (gameDetails.villain_one, gameDetails.villain_two, gameDetails.villain_three, gameDetails.villain_four, gameDetails.villain_five)'
        )

    def test_with_villain_and_opponent_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN, SqlTables.OPPONENTS)
        assert (
            test_response
            == '"Baron Blade" IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five)'
        )
