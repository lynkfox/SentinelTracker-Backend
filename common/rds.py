from typing import Union
from common.models.character_enums import (
    Character,
    AlternateTags,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)


def create_rds_key(
    full_name: Union[Character, str],
    alternate_name: Union[AlternateTags, str, None],
    mapping: dict,
) -> str:
    """
    Builds the "full_name" for a given Hero, Villain, or Environment entry in the RDS
    """
    alternate_name = ALTERNATE_TAG_DISPLAY_MAPPING.get(alternate_name)
    full_name = mapping.get(full_name)
    if alternate_name is not None:
        full_name = f"{full_name}{alternate_name}"
