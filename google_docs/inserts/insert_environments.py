import json

from dataclasses import dataclass, field
from common.models.character_enums import (
    AlternateTags,
    Location,
    EntityType,
    LOCATION_DISPLAY_MAPPING,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)
from common.models.game_details_enums import BoxSet
from google_docs.inserts.insert_heroes import _deal_with_alt_prefix
from typing import Union


@dataclass
class EnvironmentInsert:
    character: Union[Location, str]
    box_set: Union[BoxSet, str]
    alternate_name: Union[AlternateTags, str, None] = field(default=None)
    base: Union[Location, str] = field(default=None)
    full_name: str = field(init=False)
    query_name_value: str = field(init=False)
    query_alt_value: str = field(init=False)
    type: Union[EntityType, str] = field(init=False)

    def __post_init__(self):

        display_name = LOCATION_DISPLAY_MAPPING.get(self.character)
        display_alt = ALTERNATE_TAG_DISPLAY_MAPPING.get(self.alternate_name)
        is_definitive = (
            self.box_set in [BoxSet.DEFINITIVE_EDITION, BoxSet.ROOK_CITY_RENEGADES] and self.alternate_name is not AlternateTags.definitive
        )

        self.query_name_value = self.character.value

        if self.alternate_name is not None:
            self.query_alt_value = (
                f"definitive_{_deal_with_alt_prefix(self.alternate_name.value)}"
                if is_definitive
                else _deal_with_alt_prefix(self.alternate_name.value)
            )
        else:
            self.query_alt_value = None

        self.type = EntityType.LOCATION.value if is_definitive else f"definitive {EntityType.LOCATION.value}"

        self.box_set = self.box_set.value
        self.base = display_name

        if self.alternate_name is not None and is_definitive:
            self.full_name = f"{display_name}{ALTERNATE_TAG_DISPLAY_MAPPING.get(AlternateTags.definitive)}{display_alt}"
        elif self.alternate_name is not None:
            self.full_name = f"{display_name}{display_alt}"
        else:
            self.full_name = display_name


ENVIRONMENTS_TO_INSERT = [
    EnvironmentInsert(Location.block, BoxSet.SHATTERED_TIMELINES),
    EnvironmentInsert(Location.celestial_tribunal, BoxSet.CELESTIAL_TRIBUNAL),
    EnvironmentInsert(Location.champion_studios, BoxSet.OBLIVAEON),
    EnvironmentInsert(Location.court_of_blood, BoxSet.VILLAINS),
    EnvironmentInsert(Location.dok_thorath_capital, BoxSet.WRATH_OF_THE_COSMOS),
    EnvironmentInsert(Location.enclave_of_the_endlings, BoxSet.WRATH_OF_THE_COSMOS),
    EnvironmentInsert(Location.final_wasteland, BoxSet.FINAL_WASTELAND),
    EnvironmentInsert(Location.fort_adamant, BoxSet.OBLIVAEON),
    EnvironmentInsert(Location.freedom_tower, BoxSet.VENGEANCE),
    EnvironmentInsert(Location.insula_primalis, BoxSet.ENHANCED_EDITION),
    EnvironmentInsert(Location.madame_mittermeiers, BoxSet.VILLAINS),
    EnvironmentInsert(Location.maerynian_refuge, BoxSet.OBLIVAEON),
    EnvironmentInsert(Location.magmaria, BoxSet.VILLAINS),
    EnvironmentInsert(Location.megalopolis, BoxSet.ENHANCED_EDITION),
    EnvironmentInsert(Location.mobile_defense_platform, BoxSet.VENGEANCE),
    EnvironmentInsert(Location.mordengrad, BoxSet.OBLIVAEON),
    EnvironmentInsert(Location.nexus_of_the_void, BoxSet.OBLIVAEON),
    EnvironmentInsert(Location.omnitron_iv, BoxSet.OMNITRON_IV),
    EnvironmentInsert(Location.pike_industrial_complex, BoxSet.ROOK_CITY),
    EnvironmentInsert(Location.realm_of_discord, BoxSet.INFERNAL_RELICS),
    EnvironmentInsert(Location.rook_city, BoxSet.ROOK_CITY),
    EnvironmentInsert(Location.ruins_of_atlantis, BoxSet.ENHANCED_EDITION),
    EnvironmentInsert(Location.silver_gulch_1883, BoxSet.SILVER_GULCH),
    EnvironmentInsert(Location.temple_of_zhu_long, BoxSet.VILLAINS),
    EnvironmentInsert(Location.time_cataclysm, BoxSet.SHATTERED_TIMELINES),
    EnvironmentInsert(Location.tomb_of_anubis, BoxSet.INFERNAL_RELICS),
    EnvironmentInsert(Location.wagner_mars_base, BoxSet.ENHANCED_EDITION),
    EnvironmentInsert(Location.megalopolis, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    EnvironmentInsert(Location.freedom_tower, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    EnvironmentInsert(Location.insula_primalis, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    EnvironmentInsert(Location.magmaria, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    EnvironmentInsert(
        Location.ruins_of_atlantis,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(
        Location.wagner_mars_base,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(Location.blackwood_forest, BoxSet.CAULDRON),
    EnvironmentInsert(Location.f_s_c_continuance_wanderer, BoxSet.CAULDRON),
    EnvironmentInsert(Location.halberd_experimental_research_center, BoxSet.CAULDRON),
    EnvironmentInsert(Location.northspar, BoxSet.CAULDRON),
    EnvironmentInsert(Location.st_simeons_catacombs, BoxSet.CAULDRON),
    EnvironmentInsert(Location.wandering_isle, BoxSet.CAULDRON),
    EnvironmentInsert(Location.superstorm_akela, BoxSet.CAULDRON_STORMFALL),
    EnvironmentInsert(Location.cybersphere, BoxSet.CAULDRON_EXPERIMENTAL),
    EnvironmentInsert(Location.catchwater_harbor_1929, BoxSet.CAULDRON_ADRIFT),
    EnvironmentInsert(Location.chasm_of_a_thousand_nights, BoxSet.CAULDRON_ADRIFT),
    EnvironmentInsert(Location.nightlore_citadel, BoxSet.CAULDRON_ADRIFT),
    EnvironmentInsert(Location.vault_5, BoxSet.CAULDRON_ADRIFT),
    EnvironmentInsert(Location.windmill_city, BoxSet.CAULDRON_ADRIFT),
]
