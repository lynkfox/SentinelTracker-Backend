from re import S
from common.rds.queries_gen import *
import pytest


class Test_character_is:
    def test_returns_str(self):
        assert isinstance(character_is("Test"), str)

    def test_raises_value_error_on_not_type_hero(self):
        with pytest.raises(ValueError, match="[prefix] Mismatch: must be HERO or VILLAIN") as e:
            character_is("test", Type.ENVIRONMENT)

    def test_raises_value_error_on_type_villain_but__not_opponent_table(self):
        with pytest.raises(
            ValueError,
            match="[table_name] Mismatch: table_name must be GAME_DETAILS, HERO_TEAMS, or OPPONENTS",
        ) as e:
            character_is("test", Type.VILLAIN, SqlTables.HEROES)

    def test_with_hero_and_hero_teams_table_prefix_column_names_correctly(self):
        test_response = character_is("Absolute Zero", Type.HERO, SqlTables.HERO_TEAMS)
        assert (
            test_response
            == "`Absolute Zero` IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)"
        )

    def test_with_villain_and_no_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN)
        assert (
            test_response
            == "`Baron Blade` IN (gameDetails.villain_one, gameDetails.villain_two, gameDetails.villain_three, gameDetails.villain_four, gameDetails.villain_five)"
        )

    def test_with_villain_and_opponent_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN, SqlTables.OPPONENTS)
        assert (
            test_response
            == "`Baron Blade` IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five)"
        )


class Test_with_allies:
    def test_returns_str(self):
        assert isinstance(with_allies(["Absolute Zero"], Type.HERO), str)

    def test_returns_valid_string_with_only_one_hero(self):
        test_response = with_allies(["Absolute Zero"], Type.HERO)
        assert test_response == "heroTeams.hero_one=`Absolute Zero`"

    def test_returns_valid_string_with_more_than_one_hero(self):
        test_response = with_allies(["Absolute Zero", "Bunker"], Type.HERO)
        assert test_response == "heroTeams.hero_one=`Absolute Zero`, heroTeams.hero_two=`Bunker`"

    def test_same_order_if_positional_true(self):
        test_response = with_allies(["Writhe", "Bunker"], Type.HERO, positional=True)
        assert test_response == "gameDetails.hero_one=`Writhe`, gameDetails.hero_two=`Bunker`"

    def test_sorts_if_positional_left_to_default(self):
        test_response = with_allies(["Writhe", "Bunker"], Type.HERO)
        assert test_response == "heroTeams.hero_one=`Bunker`, heroTeams.hero_two=`Writhe`"

    def test_villains_points_to_opponent_table(self):
        test_response = with_allies(["Baron Blade", "Ermine"], Type.VILLAIN)
        assert test_response == "opponents.villain_one=`Baron Blade`, opponents.villain_two=`Ermine`"

    def test_raises_value_error_with_more_than_5_names(self):
        with pytest.raises(ValueError, match="[names]: too many names for with_allies") as e:
            test_response = with_allies(["", "", "", "", "", ""], Type.VILLAIN)
