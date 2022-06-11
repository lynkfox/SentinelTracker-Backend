from lambda_functions.get_entity.utilities import LookUp
from common.models.enums import Default, Comparator


class Test_Lookup:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_base_hero_path_returns_all(self):
        test_path = "/hero"
        test_lookup = LookUp(test_path)

        assert test_lookup.left_name == Default.ALL
        assert test_lookup.left_alternate == None
        assert test_lookup.first_qualifier == None

    def test_hero_path_with_name_captures_name_and_all_for_alt(self):
        test_path = "/hero/absolute_zero"
        test_lookup = LookUp(test_path)

        assert test_lookup.left_name == "absolute_zero"
        assert test_lookup.left_alternate == Default.BASE
        assert test_lookup.first_qualifier == None

    def test_hero_path_with_just_name_versus_name(self):
        test_path = "/hero/absolute_zero/versus/baron_blade"
        test_lookup = LookUp(test_path)

        assert test_lookup.left_name == "absolute_zero"
        assert test_lookup.left_alternate == Default.BASE
        assert test_lookup.first_qualifier == Comparator.VERSUS
        assert test_lookup.right_name == "baron_blade"
        assert test_lookup.right_alternate == Default.BASE
