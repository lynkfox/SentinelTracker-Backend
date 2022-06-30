from common.models.schema_models import _build_id_hash, User, OblivAeonDetail, HeroTeam, VillainOpponent, GameDetail
import pytest
from pydantic import ValidationError
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition, GameLength, GameMode, SelectionMethod
from datetime import datetime


class Test_build_id_hash:
    def test_hash_is_repeatable_and_not_randomized(self):
        # Due to the fact that Python implemented a randomized seed into their
        # hash() function that is randomized on every invocation of the
        # interpreter, we cannot rely on that in a Lambda environment to
        # generate the same hash value - which we want to use as a way to
        # provide a unique id to a set of concat'ed strings.

        known_result = -4681749772389249450
        result = _build_id_hash("Test_string to hash here we go")

        assert result == known_result


class Test_UserBaseModel:
    def test_schema_output_removes_title_from_properties(self):

        result = User.schema()

        assert result["properties"]["username"].get("title") is None


class Test_OblivAeonDetailBaseModel:
    def setup(self):
        self.test_object = OblivAeonDetail(
            scions="Scion A-Scion B-Scion C",
            shield="Shield A",
            environments="Environment A-Environment B-Environment C",
            player_one_heroes="Hero 1-Hero 2-Hero 3",
            player_two_heroes="Hero 1-Hero 2-Hero 3",
            player_three_heroes="Hero 1-Hero 2-Hero3",
            rewards="Reward A-Reward B",
        )

    def teardown(self):
        del self.test_object

    def test_generates_id_hash_automatically(self):
        assert self.test_object.id_hash is not None

    def test_id_hash_based_off_concat_of_scions_and_shield(self):
        expected_id_hash = _build_id_hash("Scion A-Scion B-Scion CShield A")
        assert self.test_object.id_hash == expected_id_hash

    def test_id_hash_not_included_in_schema_properties_but_still_has_object_attr(self):
        schema = OblivAeonDetail.schema()

        assert schema["properties"].get("id_hash") is None
        assert hasattr(self.test_object, "id_hash")


class Test_HeroTeamBaseModel:
    def setup(self):
        self.test_object = HeroTeam(hero_one="Absolute Zero", hero_two="Legacy", hero_three="Tachyon")

    def teardown(self):
        del self.test_object

    def test_creates_id_hash_automatically(self):
        self.test_object.id_hash is not None

    def test_id_hash_based_on_concat_of_all_heroes_with_dash_for_empty_slots(self):
        expected_id_hash = _build_id_hash("Absolute ZeroLegacyTachyon--")
        assert self.test_object.id_hash == expected_id_hash

    def test_schema_output_does_not_include_id_hash_though_it_remains_on_object(self):
        schema = HeroTeam.schema()

        assert schema["properties"].get("id_hash") is None
        assert hasattr(self.test_object, "id_hash")

    def test_schema_output_does_not_include_valid_team_though_it_remains_on_object(self):
        schema = HeroTeam.schema()

        assert schema["properties"].get("valid_team") is None
        assert hasattr(self.test_object, "valid_team")

    def test_raises_exception_if_not_at_least_three_heroes(self):

        with pytest.raises(ValidationError) as e:
            test_object = HeroTeam(
                hero_one="Absolute Zero",
                hero_two="Legacy",
            )

    def test_if_name_added_in_later_hero_it_collapses_team_members(self):
        # first 3 team members are required and will raise an exception if not
        test_object = HeroTeam(hero_one="Absolute Zero", hero_two="Legacy", hero_three="Tachyon", hero_four=None, hero_five="Writhe")

        assert test_object.hero_four == "Writhe"
        assert test_object.hero_five is None

    def test_object_alphabetizes_heroes(self):
        test_object = HeroTeam(hero_one="M", hero_two="Z", hero_three="A", hero_four="C")

        assert test_object.hero_one == "A"
        assert test_object.hero_two == "C"
        assert test_object.hero_three == "M"
        assert test_object.hero_four == "Z"

    def test_sets_valid_team_true_if_all_heroes_are_unique(self):
        assert self.test_object.valid_team

    def test_sets_valid_team_false_if_duplicate_hero_name(self):
        test_object = HeroTeam(hero_one="A", hero_two="Z", hero_three="A", hero_four="C")

        assert not test_object.valid_team

    def test_does_not_remove_duplicate_hero_names_on_invalid_team(self):
        test_object = HeroTeam(hero_one="A", hero_two="A", hero_three="B", hero_four="C")

        assert test_object.hero_four == "C"
        assert test_object.hero_one == "A"
        assert test_object.hero_two == "A"

    def test_valid_team_if_passed_takes_it_as_is_no_matter_hero_values(self):

        # should normally result in valid_team is False, but we're passing True
        test_object = HeroTeam(hero_one="A", hero_two="A", hero_three="B", hero_four="C", valid_team=True)

        assert test_object.valid_team

    def test_get_insert_statement_returns_an_sql_statement(self):
        expected_statement = "INSERT INTO heroTeams (hero_one, hero_two, hero_three, valid_team, id_hash) VALUES ('Absolute Zero', 'Legacy', 'Tachyon', True, -7134208906570383273)"

        assert self.test_object.get_insert_statement() == expected_statement


class Test_VillainOpponentBaseModel:
    def setup(self):
        self.test_object = VillainOpponent(villain_one="Baron Blade")

    def teardown(self):
        del self.test_object

    def test_creates_id_hash_automatically(self):
        self.test_object.id_hash is not None

    def test_id_hash_based_on_concat_of_all_heroes_with_dash_for_empty_slots(self):
        expected_id_hash = _build_id_hash("Baron Blade----True")
        assert self.test_object.id_hash == expected_id_hash

    def test_schema_output_does_not_include_id_hash_though_it_remains_on_object(self):
        schema = VillainOpponent.schema()

        assert schema["properties"].get("id_hash") is None
        assert hasattr(self.test_object, "id_hash")

    def test_schema_output_does_not_include_valid_team_though_it_remains_on_object(self):
        schema = VillainOpponent.schema()

        assert schema["properties"].get("valid_team") is None
        assert hasattr(self.test_object, "valid_team")

    def test_if_name_added_in_later_hero_it_collapses_team_members(self):
        # first 3 team members are required and will raise an exception if not
        test_object = VillainOpponent(
            villain_one="Baron Blade, Team Villain", villain_two=None, villain_three="Ermine", villain_four=None, villain_five="Plague Rat"
        )

        assert test_object.villain_two == "Ermine"
        assert test_object.villain_three == "Plague Rat"
        assert test_object.villain_five is None

    def test_object_alphabetizes_villains(self):
        test_object = VillainOpponent(villain_one="M", villain_two="Z", villain_three="A", villain_four="C")

        assert test_object.villain_one == "A"
        assert test_object.villain_two == "C"
        assert test_object.villain_three == "M"
        assert test_object.villain_four == "Z"

    def test_sets_valid_team_true_if_all_villains_are_unique(self):
        assert self.test_object.valid_team

    def test_sets_valid_team_false_if_duplicate_villain_name(self):
        test_object = VillainOpponent(villain_one="A", villain_two="Z", villain_three="A", villain_four="C")

        assert not test_object.valid_team

    def test_does_not_remove_duplicate_hero_names_on_invalid_team(self):
        test_object = VillainOpponent(villain_one="A", villain_two="A", villain_three="B", villain_four="C")

        assert test_object.villain_four == "C"
        assert test_object.villain_one == "A"
        assert test_object.villain_two == "A"

    def test_valid_team_if_passed_takes_it_as_is_no_matter_villain_values(self):

        # should normally result in valid_team is False, but we're passing True
        test_object = VillainOpponent(villain_one="A", villain_two="A", villain_three="B", villain_four="C", valid_team=True)

        assert test_object.valid_team

    def test_get_insert_statement_returns_an_sql_statement(self):
        expected_statement = "INSERT INTO opponents (villain_one, valid_team, id_hash) VALUES ('Baron Blade', True, -8658938199108491557)"

        assert self.test_object.get_insert_statement() == expected_statement


class Test_GameDetail:
    def setup(self):
        self.test_add_event = {
            "username": "Lynkfox",
            "game_mode": GameMode.NORMAL,
            "selection_method": SelectionMethod.RANDOM.value,
            "platform": "Physical",
            "end_result": HeroWinCondition.STANDARD.value,
            "estimated_time": GameLength.MORE_THAN_TWO_HOURS.value,
            "number_of_players": 1,
            "number_of_heroes": 3,
            "perceived_difficulty": 2,
            "environment": "Insula Primalis",
            "hero_one": "Absolute Zero",
            "hero_one_incapped": False,
            "hero_two": "Legacy",
            "hero_two_incapped": False,
            "hero_three": "Tachyon, Super Scientific",
            "hero_three_incapped": False,
            "villain_one": "Baron Blade",
            "villain_one_incapped": True,
            "advanced": True,
            "comment": "Test Entry",
        }

    def teardown(self):
        del self.test_add_event

    def test_no_entry_time_sets_as_datetime(self):
        test_object = GameDetail(**self.test_add_event)

        assert test_object.entered_on is not None
        assert datetime.fromisoformat(test_object.entered_on)

    def test_entry_time_provided_returns_as_is(self):
        now = datetime.now()
        self.test_add_event["entered_on"] = now
        test_object = GameDetail(**self.test_add_event)

        assert test_object.entered_on == now

    def test_one_villain_retains_game_mode_as_normal(self):
        test_object = GameDetail(**self.test_add_event)

        assert test_object.game_mode == GameMode.NORMAL.value

    def test_more_than_one_villain_automatically_changes_to_team_game_mode(self):
        self.test_add_event["villain_two"] = "Plague Rat"
        test_object = GameDetail(**self.test_add_event)

        assert test_object.game_mode == GameMode.VILLAINS.value

    def test_creates_OpponentObject_for_villain_if_not_provided(self):
        test_object = GameDetail(**self.test_add_event)

        assert isinstance(test_object.villain, VillainOpponent)

    def test_creates_HeroTeamObject_for_hero_team_if_not_provided(self):
        test_object = GameDetail(**self.test_add_event)

        assert isinstance(test_object.hero_team, HeroTeam)

    def test_if_villain_id_hash_number_in_villain_does_not_create_object(self):
        self.test_add_event["villain"] = 123456789
        test_object = GameDetail(**self.test_add_event)

        assert test_object.villain == 123456789

    def test_if_team_id_hash_number_in_hero_team_does_not_create_object(self):
        self.test_add_event["hero_team"] = 123456789
        test_object = GameDetail(**self.test_add_event)

        assert test_object.hero_team == 123456789

    def test_win_set_true_if_HeroWinCondition_in_end_result(self):
        self.test_add_event["end_result"] = HeroWinCondition.GLOOMWEAVER
        test_object = GameDetail(**self.test_add_event)

        assert test_object.win

    def test_win_set_true_if_HeroWinCondition_string_in_end_result(self):
        self.test_add_event["end_result"] = HeroWinCondition.GLOOMWEAVER.value
        test_object = GameDetail(**self.test_add_event)

        assert test_object.win

    def test_win_set_false_if_HeroLossCondition_in_end_result(self):
        self.test_add_event["end_result"] = HeroLossCondition.OBILVAEON
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.win

    def test_win_set_false_if_HeroLossCondition__string_in_end_result(self):
        self.test_add_event["end_result"] = HeroLossCondition.OBILVAEON.value
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.win

    def test_respects_win_if_passed_directly_without_changing_it(self):
        # loss value but win is set to true, so win should remain true
        self.test_add_event["end_result"] = HeroLossCondition.OBILVAEON
        self.test_add_event["win"] = True
        test_object = GameDetail(**self.test_add_event)

        assert test_object.win

    def test_entry_is_valid_respects_value_passed(self):
        self.test_add_event["entry_is_valid"] = False
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.entry_is_valid

    def test_entry_is_valid_automatically_false_if_house_rules_true(self):
        self.test_add_event["entry_is_valid"] = True
        self.test_add_event["house_rules"] = True
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.entry_is_valid

    def test_entry_is_valid_automatically_false_if_house_rules_is_not_None(self):
        self.test_add_event["entry_is_valid"] = True
        self.test_add_event["house_rules"] = "6 players, all Freedom Six"
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.entry_is_valid

    def test_entry_is_valid_false_if_hero_team_not_valid_team(self):
        self.test_add_event["hero_two"] = "Absolute Zero"
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.entry_is_valid

    def test_entry_is_valid_false_if_more_villains_than_heroes(self):
        self.test_add_event["villain_two"] = "Plague Rat"
        self.test_add_event["villain_three"] = "Ambuscade, Team Villain"
        self.test_add_event["villain_four"] = "The Operative"
        self.test_add_event["villain_five"] = "Ermine"
        test_object = GameDetail(**self.test_add_event)

        assert not test_object.entry_is_valid

    def test_get_insert_statement(self):
        test_object = GameDetail(**self.test_add_event)
        expected_statement = "INSERT INTO gameDetails (username, game_mode, selection_method, platform, end_result, win, estimated_time, number_of_players, number_of_heroes, perceived_difficulty, hero_team, environment, villain, hero_one, hero_one_incapped, hero_two, hero_two_incapped, hero_three, hero_three_incapped, villain_one, villain_one_incapped, advanced, comments, entry_is_valid) VALUES ('Lynkfox', 'Normal', 'Random', 'Physical', 'The Hero's Triumph (Villain(s) Incapacitated)', True, 'More than 2 hours', 1, 3, 2, -2505219922851692492, 'Insula Primalis', -8658938199108491557, 'Absolute Zero', False, 'Legacy', False, 'Tachyon, Super Scientific', False, 'Baron Blade', True, True, 'Test Entry', True)"

        assert not test_object.get_insert_statement() == expected_statement
