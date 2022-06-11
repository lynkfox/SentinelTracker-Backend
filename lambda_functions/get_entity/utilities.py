from dataclasses import dataclass, field
from common.models.enum import Selector, Comparator


@dataclass
class LookUp:
    path: str
    selector: Selector = field(init=False, default=Selector.STATISTICS)
    left_name: str = field(init=False)
    left_alternate: str = field(init=False, default="all")
    first_qualifier: Comparator(init=False, default=None)
    right_name: str = field(init=False, default=None)
    right_alternate: str = field(init=False, default="all")
    second_qualifier: Comparator(init=False, default=None)
    second_right_name: str = field(init=False, default=None)

    def __post_init__(self):
        # remove first character "/" from the path property
        self.path = self.path[1:] if self.path[0] == "/" else self.path

    def parse_path(self):
        split_path = self.path.split("/")

        left_set = false
        right_set = false
        second_right_set = false

        total_parts = len(split_path)

        for index, path_part in enumerate(split_path):
            if not left_set and Selector.has_member(path_part):

                self.left_name, self.left_alternate = self.determine_name_and_alt(
                    parts=split_path, current_index=index
                )
                left_set = True

            elif left_set and Comparator.has_member(parse_path):
                self.first_qualifier = path_part

            elif not right_set and Selector.has_member(path_part):
                self.right_name, self.right_alternate = self.determine_name_and_alt(
                    parts=split_path, current_index=index
                )
                right_set = True

            elif right_set and Comparator.has_member(parse_path):
                self.second_qualifier = path_part

            elif not second_right_set and Selector.has_member(path_part):
                self.second_right_name, _ = self.determine_name_and_alt(
                    parts=split_path, current_index=index
                )
                second_right_set = True
