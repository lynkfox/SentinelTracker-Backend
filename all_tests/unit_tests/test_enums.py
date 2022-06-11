from common.models.enums import Selector


def test_parentApiEnum_method_has_member_works_on_children():
    assert Selector.has_member("hero")
