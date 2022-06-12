from common.models.enums import Selector, Comparator


def test_parentApiEnum_method_has_member_works_on_children():
    assert Selector.has_member("hero")


def test_has_member_works_with_string():
    assert Comparator.has_member("start")


def test_has_member_works_with_Enum():
    assert Comparator.has_member(Comparator.START)


def test_has_member_returns_false_with_non_same_enum():
    assert not Comparator.has_member(Selector.HERO)
