from lambda_functions.get_entity.utilities import LookUp
from common.models.enums import Default, Comparator


class Test_Lookup:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_just_simple_path_of_type_returns_just_start_instruction_of_all(self):
        test_path = "/hero"
        test_lookup = LookUp(test_path)

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0].instruction == Comparator.START
        assert test_lookup.operations[0].name_selection == Default.ALL
        assert test_lookup.operations[0].alternate_selection is None

        # test_path = "/hero/absolute_zero"

        # test_path = "/hero/absolute_zero/versus/baron_blade"
        # test_lookup = LookUp(test_path)
