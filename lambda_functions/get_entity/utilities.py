from dataclasses import dataclass, field
from common.models.enums import Selector, Comparator, Default
from typing import Union


@dataclass
class LookUp:
    path: str
    left_selector: Selector = field(init=False, default=Selector.HERO)
    left_name: Union[str, Default, None] = field(init=False, default=None)
    left_alternate: Union[str, Default, None] = field(init=False, default=None)
    first_qualifier: Comparator = field(init=False, default=None)
    right_selector: Union[Selector, None] = field(init=False, default=None)
    right_name: Union[str, Default, None] = field(init=False, default=None)
    right_alternate: Union[str, Default, None] = field(init=False, default=None)
    second_qualifier: Comparator = field(init=False, default=None)
    second_selector: Union[Selector, None] = field(init=False, default=None)
    second_right_name: Union[str, Default, None] = field(init=False, default=None)
    path_part: list = field(init=False, default_factory=list)
    total_parts: int = field(init=False, default=0)

    def __post_init__(self):
        # remove first character "/" from the path property
        self.path = self.path[1:] if self.path[0] == "/" else self.path
        self.path_parts = self.path.split("/")
        self.total_parts = len(self.path_parts)
        self.parse_path()

    def parse_path(self):
        left_set = False
        right_set = False
        second_right_set = False

        for index, path_part in enumerate(self.path_parts):
            if not left_set and Selector.has_member(path_part):

                self.left_name, self.left_alternate = self._determine_name_and_alt(
                    current_index=index
                )
                self.left_selector = Selector(path_part)
                left_set = True

            elif (left_set and not right_set) and Comparator.has_member(path_part):
                self.first_qualifier = Comparator(path_part)
                self.right_name, self.right_alternate = self._determine_name_and_alt(
                    current_index=index
                )
                self.right_selector = self._determine_selector(self.first_qualifier)
                right_set = True

            elif (right_set and not second_right_set) and Comparator.has_member(
                path_part
            ):
                self.second_right_name, _ = self._determine_name_and_alt(
                    current_index=index
                )
                self.second_qualifier = Comparator(path_part)
                self.second_selector = self._determine_selector(self.second_qualifier)
                second_right_set = True
            else:
                continue

    def _determine_selector(self, comparison: Comparator) -> Selector:
        """
        depending on the Comparator returns the Selector
        """
        if comparison == Comparator.IN:
            return Selector.ENVIRONMENT
        if comparison == Comparator.VERSUS:
            return (
                Selector.HERO
                if self.left_selector is Selector.VILLAIN
                else Selector.VILLAIN
            )
        if comparison == Comparator.WITH:
            return self.left_selector

    def _determine_name_and_alt(self, current_index: int) -> (str, str):
        """
        picks up the next two iterations of the path parts and returns them or defaults.
        """
        next_index = current_index + 1
        second_index = current_index + 2
        if self.total_parts > next_index:
            next_part = self.path_parts[next_index]
            base_name = (
                next_part if not Comparator.has_member(next_part) else Default.ALL
            )

        else:
            base_name = Default.ALL

        if self.total_parts > second_index and base_name is not Default.ALL:
            second_part = self.path_parts[second_index]
            alt_name = (
                second_part if not Comparator.has_member(second_part) else Default.BASE
            )
        elif self.total_parts == second_index:
            alt_name = Default.BASE
        else:
            alt_name = None

        return base_name, alt_name


if __name__ == "__main__":

    LookUp("/hero/absolute_zero/versus/baron_blade")
