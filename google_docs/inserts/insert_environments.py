import json

from dataclasses import dataclass, field
from common.models.character_enums import AlternateTags, Environment, ENVIRONMENT_DISPLAY_MAPPING, ALTERNATE_TAG_DISPLAY_MAPPING
from common.models.enums import BoxSet
from typing import Union

@dataclass
class EnvironmentInsert():
    full_name: Union[Environment, str]
    box_set: Union[BoxSet, str]
    alternate_name:Union[AlternateTags, str, None] = field(default=None)
    dynamo_meta_query: str = field(init=False)

    def __post_init__(self):
        self.box_set = self.box_set.value
        query = {
            "pk": f"ENVIRONMENT#{self.full_name.value.upper()}",
            "sk": f"META#ENVIRONMENT" if self.alternate_name is None else f"META#ENVIRONMENT#ALT#{_deal_with_definitive(self.alternate_name.value).upper()}"
        }
        self.alternate_name = ALTERNATE_TAG_DISPLAY_MAPPING.get(self.alternate_name)
        self.full_name = ENVIRONMENT_DISPLAY_MAPPING.get(self.full_name)
        self.dynamo_meta_query = json.dumps(query)
        if self.alternate_name is not None:
            self.full_name = f"{self.full_name}{self.alternate_name}"

def _deal_with_definitive(name:str):
    key = "definitive_"
    if name.startswith(key):
        return name.replace(key, "{key[-1]}#")
    else:
        return name


ENVIRONMENTS_TO_INSERT = [
    EnvironmentInsert(
        Environment.the_block,
        BoxSet.SHATTERED_TIMELINES
    ),
    EnvironmentInsert(
        Environment.celestial_tribunal,
        BoxSet.CELESTIAL_TRIBUNAL
    ),
    EnvironmentInsert(
        Environment.champion_studios,
        BoxSet.OBLIVAEON
    ),
    EnvironmentInsert(
        Environment.court_of_blood,
        BoxSet.VILLAINS
    ),
    EnvironmentInsert(
        Environment.dok_thorath_capital,
        BoxSet.WRATH_OF_THE_COSMOS
    ),
    EnvironmentInsert(
        Environment.enclave_of_the_endlings,
        BoxSet.WRATH_OF_THE_COSMOS
    ),
    EnvironmentInsert(
        Environment.the_final_wasteland,
        BoxSet.FINAL_WASTELAND
    ),
    EnvironmentInsert(
        Environment.fort_adamant,
        BoxSet.OBLIVAEON
    ),
    EnvironmentInsert(
        Environment.freedom_tower,
        BoxSet.VENGEANCE
    ),
    EnvironmentInsert(
        Environment.insula_primalis,
        BoxSet.ENHANCED_EDITION
    ),
    EnvironmentInsert(
        Environment.madame_mittermeiers,
        BoxSet.VILLAINS
    ),
    EnvironmentInsert(
        Environment.maerynian_refuge,
        BoxSet.OBLIVAEON
    ),
    EnvironmentInsert(
        Environment.magmaria,
        BoxSet.VILLAINS
    ),
    EnvironmentInsert(
        Environment.megalopolis,
        BoxSet.ENHANCED_EDITION
    ),
    EnvironmentInsert(
        Environment.mobile_defense_platform,
        BoxSet.VENGEANCE
    ),
    EnvironmentInsert(
        Environment.mordengrad,
        BoxSet.OBLIVAEON
    ),
    EnvironmentInsert(
        Environment.nexus_of_the_void,
        BoxSet.OBLIVAEON
    ),
    EnvironmentInsert(
        Environment.omnitron_iv,
        BoxSet.OMNITRON_IV
    ),
    EnvironmentInsert(
        Environment.pike_industrial_complex,
        BoxSet.ROOK_CITY
    ),
    EnvironmentInsert(
        Environment.realm_of_discord,
        BoxSet.INFERNAL_RELICS
    ),
    EnvironmentInsert(
        Environment.rook_city,
        BoxSet.ROOK_CITY
    ),
    EnvironmentInsert(
        Environment.ruins_of_atlantis,
        BoxSet.ENHANCED_EDITION
    ),
    EnvironmentInsert(
        Environment.silver_gulch_1883,
        BoxSet.SILVER_GULCH
    ),
    EnvironmentInsert(
        Environment.temple_of_zhu_long,
        BoxSet.VILLAINS
    ),
    EnvironmentInsert(
        Environment.time_cataclysm,
        BoxSet.SHATTERED_TIMELINES
    ),
    EnvironmentInsert(
        Environment.tomb_of_anubis,
        BoxSet.INFERNAL_RELICS
    ),
    EnvironmentInsert(
        Environment.wagner_mars_base,
        BoxSet.ENHANCED_EDITION
    ),
    EnvironmentInsert(
        Environment.megalopolis,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    ),
    EnvironmentInsert(
        Environment.freedom_tower,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    ),
    EnvironmentInsert(
        Environment.insula_primalis,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    ),
    EnvironmentInsert(
        Environment.magmaria,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    ),
    EnvironmentInsert(
        Environment.ruins_of_atlantis,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    ),
    EnvironmentInsert(
        Environment.wagner_mars_base,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive
    )
    
]