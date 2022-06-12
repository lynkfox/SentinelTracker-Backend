from lambda_functions.get_entity.utilities import LookUp, Operation
from common.models.enums import Default, Comparator, Type, Selector
from common.models.character_enums import Hero, Villain, Environment, AlternateTags


class Test_Lookup:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_just_selector_no_character_name(self):
        test_path = "/hero"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Default.ALL, None)

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_character_name_with_no_alt(self):
        test_path = "/hero/absolute_zero"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_character_name_with_alt(self):
        test_path = "/hero/absolute_zero/freedom_six"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_character_with_no_alt_vrs_none(self):
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

    def test_character_with_alt_vrs_none(self):
        test_path = "/hero/absolute_zero/freedom_six/versus"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.VERSUS, Selector.VILLAIN, Default.ALL, None
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_vrs_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/versus/baron_blade"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.VERSUS, Selector.VILLAIN, Villain.baron_blade, Default.BASE
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_vrs_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/freedom_six/versus/baron_blade"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.VERSUS, Selector.VILLAIN, Villain.baron_blade, Default.BASE
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_vrs_character_with_alt(self):
        test_path = "/hero/absolute_zero/versus/baron_blade/mad_bomber"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.VERSUS,
            Selector.VILLAIN,
            Villain.baron_blade,
            AlternateTags.mad_bomber,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_vrs_character_with_alt(self):
        test_path = "/hero/absolute_zero/freedom_six/versus/baron_blade/mad_bomber"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.VERSUS,
            Selector.VILLAIN,
            Villain.baron_blade,
            AlternateTags.mad_bomber,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_in_no_env(self):
        test_path = "/hero/absolute_zero/in"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.IN, Selector.ENVIRONMENT, Default.ALL, None
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_in_no_env(self):
        test_path = "/hero/absolute_zero/freedom_six/in"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.IN, Selector.ENVIRONMENT, Default.ALL, None
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_in_environment(self):
        test_path = "/hero/absolute_zero/in/insula_primalis"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.IN,
            Selector.ENVIRONMENT,
            Environment.insula_primalis,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_in_environment(self):
        test_path = "/hero/absolute_zero/freedom_six/in/insula_primalis"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.IN,
            Selector.ENVIRONMENT,
            Environment.insula_primalis,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_with_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/with/tachyon"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_with_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/freedom_six/with/tachyon"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_with_character_with_alt(self):
        test_path = "/hero/absolute_zero/with/tachyon/freedom_six"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE
        )
        operation_two = Operation(
            Comparator.WITH, Selector.HERO, Hero.tachyon, AlternateTags.freedom_six
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_alt_with_character_with_alt(self):
        test_path = "/hero/absolute_zero/freedom_six/with/tachyon/freedom_six"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            AlternateTags.freedom_six,
        )
        operation_two = Operation(
            Comparator.WITH, Selector.HERO, Hero.tachyon, AlternateTags.freedom_six
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two
