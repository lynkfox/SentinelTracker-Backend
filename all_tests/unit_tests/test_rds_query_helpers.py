from common.rds import LookUp
import pytest
from common.rds.queries_gen import *


class Test_character_is:
    def test_returns_str(self):
        assert isinstance(character_is("Test"), str)

    def test_raises_value_error_on_not_type_hero(self):
        with pytest.raises(ValueError, match="prefix Mismatch: must be HERO or VILLAIN") as e:
            character_is("test", Type.LOCATION)

    def test_raises_value_error_on_type_villain_but__not_opponent_table(self):
        with pytest.raises(
            ValueError,
            match="table_name Mismatch: table_name must be GAME_DETAILS, HERO_TEAMS, or OPPONENTS",
        ) as e:
            character_is("test", Type.VILLAIN, SqlTables.HEROES)

    def test_with_hero_and_hero_teams_table_prefix_column_names_correctly(self):
        test_response = character_is("Absolute Zero", Type.HERO, SqlTables.HERO_TEAMS)
        assert (
            test_response
            == "'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)"
        )

    def test_with_villain_and_no_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN)
        assert (
            test_response
            == "'Baron Blade' IN (gameDetails.villain_one, gameDetails.villain_two, gameDetails.villain_three, gameDetails.villain_four, gameDetails.villain_five)"
        )

    def test_with_villain_and_opponent_table_returns_correct_string(self):
        test_response = character_is("Baron Blade", Type.VILLAIN, SqlTables.OPPONENTS)
        assert (
            test_response
            == "'Baron Blade' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five)"
        )


class Test_team_is:
    def test_returns_str(self):
        assert isinstance(team_is(["Absolute Zero"], Type.HERO), str)

    def test_returns_valid_string_with_only_one_hero(self):
        test_response = team_is(["Absolute Zero"], Type.HERO)
        assert (
            test_response
            == "'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)"
        )

    def test_returns_valid_string_with_more_than_one_hero(self):
        test_response = team_is(["Absolute Zero", "Bunker"], Type.HERO)
        assert (
            test_response
            == "'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Bunker' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)"
        )

    def test_same_order_if_positional_true(self):
        test_response = team_is(["Writhe", "Bunker"], Type.HERO, positional=True)
        assert test_response == "gameDetails.hero_one='Writhe', gameDetails.hero_two='Bunker'"

    def test_sorts_if_positional_left_to_default(self):
        test_response = team_is(["Legacy", "Bunker"], Type.HERO)
        assert (
            test_response
            == "'Bunker' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Legacy' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five)"
        )

    def test_villains_points_to_opponent_table(self):
        test_response = team_is(["Baron Blade", "Ermine"], Type.VILLAIN)
        assert (
            test_response
            == "'Baron Blade' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five) AND 'Ermine' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five)"
        )

    def test_raises_value_error_with_more_than_5_names(self):
        with pytest.raises(ValueError, match="names: too many names for team_is") as e:
            team_is(["", "", "", "", "", ""], Type.VILLAIN)


class Test_in_environment:
    def test_returns_a_string(self):
        assert isinstance(in_location("Insula Primalis"), str)

    def test_returns_a_valid_qualifier(self):
        test_result = in_location("Insula Primalis")
        assert test_result == "gameDetails.environment='Insula Primalis'"


class Test_generate_from_operations:
    def test_single_base_hero_generates_good_sql_select_query(self):
        operations = LookUp("hero/absolute_zero").operations

        test_result = generate_from_operations(operations)

        assert test_result == (
            "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.entry_is_valid"
        )

    def test_multiple_base_heroes(self):
        operations = LookUp("hero/absolute_zero/with/bunker").operations

        test_result = generate_from_operations(operations)

        assert test_result == (
            "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Bunker' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.entry_is_valid"
        )

    def test_single_hero_alternate(self):
        operations = LookUp("hero/absolute_zero/freedom_six").operations

        test_result = generate_from_operations(operations)

        assert test_result == (
            "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero, Freedom Six' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.entry_is_valid"
        )

    def test_single_hero_definite(self):
        operations = LookUp("hero/absolute_zero/definitive").operations

        test_result = generate_from_operations(operations)

        assert test_result == (
            "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero, Definitive' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.entry_is_valid"
        )

    def test_multiple_heroes_with_alts(self):
        operations = LookUp("hero/absolute_zero/freedom_six/with/legacy/americas_greatest").operations

        test_result = generate_from_operations(operations)

        assert test_result == (
            "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero, Freedom Six' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Legacy, America's Greatest' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.entry_is_valid"
        )

    def test_single_villain(self):
        operations = LookUp("villain/baron_blade").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Baron Blade' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five) AND gameDetails.entry_is_valid"
        )

    def test_single_environment(self):
        operations = LookUp("environment/insula_primalis").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE gameDetails.environment='Insula Primalis' AND gameDetails.entry_is_valid"
        )

    def test_hero_versus_villain(self):
        operations = LookUp("hero/absolute_zero/versus/baron_blade").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Baron Blade' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five) AND gameDetails.entry_is_valid"
        )

    def test_hero_versus_villain_in_env(self):
        operations = LookUp("hero/absolute_zero/versus/baron_blade/in/insula_primalis").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND 'Baron Blade' IN (opponents.villain_one, opponents.villain_two, opponents.villain_three, opponents.villain_four, opponents.villain_five) AND gameDetails.environment='Insula Primalis' AND gameDetails.entry_is_valid"
        )

    def test_user(self):
        operations = LookUp("user/Lynkfox").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE gameDetails.username='Lynkfox' AND gameDetails.entry_is_valid"
        )

    def test_hero_from_user(self):
        operations = LookUp("hero/absolute_zero/from/Lynkfox").operations

        test_result = generate_from_operations(operations)

        assert (
            test_result
            == "SELECT * from gameDetails INNER JOIN heroTeams on heroTeams.id_hash = gameDetails.hero_team INNER JOIN opponents on opponents.id_hash = gameDetails.villain WHERE 'Absolute Zero' IN (heroTeams.hero_one, heroTeams.hero_two, heroTeams.hero_three, heroTeams.hero_four, heroTeams.hero_five) AND gameDetails.username='Lynkfox' AND gameDetails.entry_is_valid"
        )


def test_query():
    from common.rds import get_mysql_client
    from common.rds.queries import query

    operations = LookUp("hero/absolute_zero/from/Lynkfox").operations
    response = query(operations, get_mysql_client())
    assert response
