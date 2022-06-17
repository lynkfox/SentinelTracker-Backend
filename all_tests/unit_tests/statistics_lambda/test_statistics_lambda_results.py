from lambda_functions.statistics.results import _is_win_condition
from common.models.game_details_enums import HeroWinCondition, HeroLossCondition


class Test_is_win_condition:
    def test_returns_true_for_HeroWinCondtion_as_string(self):
        assert _is_win_condition("The Hero's Triumph (Villain(s) Incapacitated)")

    def test_returns_false_for_HeroLossCondtion_as_string(self):
        assert not _is_win_condition("Heroes Defeated by the Villains")

    def test_returns_true_for_HeroWinCondtion_as_enum(self):
        assert _is_win_condition(HeroWinCondition.STANDARD)

    def test_returns_false_for_HeroLossCondtion_as_enum(self):
        assert not _is_win_condition(HeroLossCondition.BARON_BLADE)
