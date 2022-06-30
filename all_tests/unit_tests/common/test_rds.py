from common.rds import LookUp, Operation, character_full_name, character_full_name_to_enums
from common.models.enums import Default, Comparator, Type, Selector
from common.models.character_enums import (
    Hero,
    Villain,
    Location,
    AlternateTags,
    HERO_DISPLAY_MAPPING,
    VILLAIN_DISPLAY_MAPPING,
    LOCATION_DISPLAY_MAPPING,
)


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
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)

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
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.VERSUS, Selector.OPPONENT, Default.ALL, None)

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
        operation_two = Operation(Comparator.VERSUS, Selector.OPPONENT, Default.ALL, None)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_vrs_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/versus/baron_blade"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.VERSUS, Selector.OPPONENT, Villain.baron_blade, Default.BASE)

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
        operation_two = Operation(Comparator.VERSUS, Selector.OPPONENT, Villain.baron_blade, Default.BASE)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_vrs_character_with_alt(self):
        test_path = "/hero/absolute_zero/versus/baron_blade/mad_bomber"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(
            Comparator.VERSUS,
            Selector.OPPONENT,
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
            Selector.OPPONENT,
            Villain.baron_blade,
            AlternateTags.mad_bomber,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_in_no_env(self):
        test_path = "/hero/absolute_zero/in"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.IN, Selector.LOCATION, Default.ALL, None)

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
        operation_two = Operation(Comparator.IN, Selector.LOCATION, Default.ALL, None)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_in_environment(self):
        test_path = "/hero/absolute_zero/in/insula_primalis"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(
            Comparator.IN,
            Selector.LOCATION,
            Location.insula_primalis,
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
            Selector.LOCATION,
            Location.insula_primalis,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_with_character_with_no_alt(self):
        test_path = "/hero/absolute_zero/with/tachyon"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE)

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
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_no_alt_with_character_with_alt(self):
        test_path = "/hero/absolute_zero/with/tachyon/freedom_six"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, AlternateTags.freedom_six)

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
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, AlternateTags.freedom_six)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_character_with_character_versus_character(self):
        test_path = "/hero/absolute_zero/with/tachyon/versus/baron_blade"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            Default.BASE,
        )
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE)

        operation_three = Operation(
            Comparator.VERSUS,
            Selector.OPPONENT,
            Villain.baron_blade,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 3
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two
        assert test_lookup.operations[2] == operation_three

    def test_character_with_character_versus_character_in_environment(self):
        test_path = "/hero/absolute_zero/with/tachyon/versus/baron_blade/in/insula_primalis"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.HERO,
            Hero.absolute_zero,
            Default.BASE,
        )
        operation_two = Operation(Comparator.WITH, Selector.HERO, Hero.tachyon, Default.BASE)

        operation_three = Operation(
            Comparator.VERSUS,
            Selector.OPPONENT,
            Villain.baron_blade,
            Default.BASE,
        )
        operation_four = Operation(
            Comparator.IN,
            Selector.LOCATION,
            Location.insula_primalis,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 4
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two
        assert test_lookup.operations[2] == operation_three
        assert test_lookup.operations[3] == operation_four

    def test_environment_with_character(self):
        test_path = "/environment/insula_primalis/with/absolute_zero"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.LOCATION,
            Location.insula_primalis,
            Default.BASE,
        )

        operation_two = Operation(
            Comparator.WITH,
            Selector.HERO,
            Hero.absolute_zero,
            Default.BASE,
        )

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two

    def test_definitive_prefix_on_existing_alternate(self):
        test_path = "/villain/baron_blade/definitive_mad_bomber"
        test_lookup = LookUp(test_path)
        operation_one = Operation(
            Comparator.START,
            Selector.OPPONENT,
            Villain.baron_blade,
            AlternateTags.mad_bomber,
            True,
        )

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_character_with_just_definitive(self):
        test_path = "/villain/baron_blade/definitive"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.OPPONENT, Villain.baron_blade, Default.BASE, True)

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_username(self):
        test_path = "/user/Lynkfox"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.USER, "Lynkfox", Default.BASE, False)

        assert len(test_lookup.operations) == 1
        assert test_lookup.operations[0] == operation_one

    def test_hero_from_username(self):
        test_path = "/hero/absolute_zero/from/Lynkfox"
        test_lookup = LookUp(test_path)
        operation_one = Operation(Comparator.START, Selector.HERO, Hero.absolute_zero, Default.BASE)
        operation_two = Operation(Comparator.FROM, Selector.USER, "Lynkfox", Default.BASE, False)

        assert len(test_lookup.operations) == 2
        assert test_lookup.operations[0] == operation_one
        assert test_lookup.operations[1] == operation_two


class Test_character_full_name:
    def test_single_name(self):
        test_response = character_full_name(Hero.absolute_zero, None, mapping=HERO_DISPLAY_MAPPING)

        assert test_response == "Absolute Zero"

    def test_name_with_alternate(self):
        test_response = character_full_name(Hero.absolute_zero, AlternateTags.freedom_five, mapping=HERO_DISPLAY_MAPPING)

        assert test_response == "Absolute Zero, Freedom Five"

    def test_name_with_alternate_and_is_definitive(self):
        test_response = character_full_name(Hero.absolute_zero, AlternateTags.first_appearance, mapping=HERO_DISPLAY_MAPPING, is_definitive=True)

        assert test_response == "Absolute Zero, Definitive, First Appearance of"


class Test_character_full_name_to_enums:
    def test_single_name(self):
        test_response = character_full_name_to_enums("Absolute Zero", mapping=HERO_DISPLAY_MAPPING)

        assert test_response == (Hero.absolute_zero, [None])

    def test_name_with_alternate_tag(self):
        test_response = character_full_name_to_enums("Absolute Zero, Freedom Five", mapping=HERO_DISPLAY_MAPPING)

        assert test_response == (Hero.absolute_zero, [AlternateTags.freedom_five])

    def test_definitive_base_hero(self):
        test_response = character_full_name_to_enums("Absolute Zero, Definitive", mapping=HERO_DISPLAY_MAPPING)

        assert test_response == (Hero.absolute_zero, [AlternateTags.definitive])

    def test_definitive_base_hero_with_alternate_tag(self):
        test_response = character_full_name_to_enums("Absolute Zero, Definitive, First Appearance of", mapping=HERO_DISPLAY_MAPPING)

        assert test_response == (Hero.absolute_zero, [AlternateTags.definitive, AlternateTags.first_appearance])

    def test_bad_input_returns_none(self):
        test_response = character_full_name_to_enums("adfasdf, adsfaew", mapping=HERO_DISPLAY_MAPPING)

        assert test_response == (None, [None])
