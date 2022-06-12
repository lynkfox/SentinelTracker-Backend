from lambda_functions.get_entity.utilities import LookUp, Operation
from common.models.enums import Default, Comparator, Type, Selector
from common.models.character_enums import Hero, Villain, Environment


class Test_Lookup:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_just_simple_path_of_type_returns_just_start_instruction_of_all(self):
        test_path = "/hero"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Default.ALL, None)

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_single_character_with_name(self):
        test_path = "/hero/absolute_zero"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_single_character_vrsus_none(self):
        test_path = "/hero/absolute_zero/versus"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.VERSUS, Selector.VILLAIN, Default.ALL, None
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two
        # assert test_lookup.operations[1].
