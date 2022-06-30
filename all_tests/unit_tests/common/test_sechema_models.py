from common.models.schema_models import _build_id_hash, User, OblivAeonDetail, HeroTeam, VillainOpponent, GameDetail
import pytest
from pydantic import ValidationError


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
