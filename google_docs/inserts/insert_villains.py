import json

from dataclasses import dataclass, field
from common.dynamo import build_pk, build_meta_sk
from common.models.character_enums import (
    AlternateTags,
    Villain,
    VILLAIN_DISPLAY_MAPPING,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)
from common.models.game_details_enums import BoxSet
from common.models.enums import Type
from typing import Union


@dataclass
class VillainInsert:
    full_name: Union[Villain, str]
    box_set: Union[BoxSet, str]
    alternate_name: Union[AlternateTags, str, None] = field(default=None)
    dynamo_meta_query: str = field(init=False)

    def __post_init__(self):
        query = {
            "pk": build_pk(
                self.full_name, self.alternate_name, self.box_set, Type.VILLAIN
            ),
            "sk": build_meta_sk(self.alternate_name),
        }
        self.box_set = self.box_set.value
        self.alternate_name = ALTERNATE_TAG_DISPLAY_MAPPING.get(self.alternate_name)
        self.full_name = VILLAIN_DISPLAY_MAPPING.get(self.full_name)
        self.dynamo_meta_query = json.dumps(query)
        if self.alternate_name is not None:
            self.full_name = f"{self.full_name}{self.alternate_name}"


VILLAINS_TO_INSERT = [
    VillainInsert(Villain.aeon_master, BoxSet.OBLIVAEON),
    VillainInsert(Villain.akash_bhuta, BoxSet.INFERNAL_RELICS),
    VillainInsert(
        Villain.akash_bhuta, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(Villain.akash_bhuta, BoxSet.DEFINITIVE_EDITION, AlternateTags.mecha),
    VillainInsert(Villain.ambuscade, BoxSet.AMBUSCADE),
    VillainInsert(Villain.ambuscade, BoxSet.AMBUSCADE, AlternateTags.team_villain),
    VillainInsert(Villain.apostate, BoxSet.INFERNAL_RELICS),
    VillainInsert(Villain.baron_blade, BoxSet.ENHANCED_EDITION),
    VillainInsert(
        Villain.baron_blade, BoxSet.ENHANCED_EDITION, AlternateTags.mad_bomber
    ),
    VillainInsert(Villain.baron_blade, BoxSet.VENGEANCE, AlternateTags.team_villain),
    VillainInsert(
        Villain.baron_blade, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(
        Villain.baron_blade,
        BoxSet.DEFINITIVE_EDITION,
        AlternateTags.definitive_mad_bomber,
    ),
    VillainInsert(Villain.biomancer, BoxSet.VILLAINS),
    VillainInsert(Villain.borr_the_unstable, BoxSet.OBLIVAEON),
    VillainInsert(Villain.bugbear, BoxSet.VILLAINS),
    VillainInsert(Villain.chairman, BoxSet.ROOK_CITY),
    VillainInsert(Villain.chokepoint, BoxSet.CHOKEPOINT),
    VillainInsert(Villain.citizen_dawn, BoxSet.ENHANCED_EDITION),
    VillainInsert(
        Villain.citizen_dawn, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(
        Villain.citizen_dawn, BoxSet.DEFINITIVE_EDITION, AlternateTags.sunrise
    ),
    VillainInsert(Villain.citizens_hammer_and_anvil, BoxSet.VILLAINS),
    VillainInsert(Villain.dark_mind, BoxSet.OBLIVAEON),
    VillainInsert(Villain.deadline, BoxSet.WRATH_OF_THE_COSMOS),
    VillainInsert(Villain.the_dreamer, BoxSet.SHATTERED_TIMELINES),
    VillainInsert(Villain.empyreon, BoxSet.OBLIVAEON),
    VillainInsert(Villain.the_ennead, BoxSet.INFERNAL_RELICS),
    VillainInsert(Villain.ermine, BoxSet.VENGEANCE),
    VillainInsert(Villain.faultless, BoxSet.OBLIVAEON),
    VillainInsert(Villain.friction, BoxSet.VENGEANCE),
    VillainInsert(Villain.fright_train, BoxSet.VENGEANCE),
    VillainInsert(Villain.gloomweaver, BoxSet.INFERNAL_RELICS),
    VillainInsert(
        Villain.gloomweaver, BoxSet.INFERNAL_RELICS, AlternateTags.skinwalker
    ),
    VillainInsert(Villain.grand_warlord_voss, BoxSet.ENHANCED_EDITION),
    VillainInsert(Villain.grand_warlord_voss, BoxSet.OBLIVAEON, AlternateTags.scion),
    VillainInsert(
        Villain.grand_warlord_voss, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(
        Villain.grand_warlord_voss, BoxSet.DEFINITIVE_EDITION, AlternateTags.censor
    ),
    VillainInsert(Villain.greazer_clutch, BoxSet.VILLAINS),
    VillainInsert(Villain.infinitor, BoxSet.WRATH_OF_THE_COSMOS),
    VillainInsert(Villain.infinitor, BoxSet.WRATH_OF_THE_COSMOS, AlternateTags.heroic),
    VillainInsert(Villain.iron_legacy, BoxSet.SHATTERED_TIMELINES),
    VillainInsert(Villain.kaargra_warfang, BoxSet.WRATH_OF_THE_COSMOS),
    VillainInsert(Villain.kismet, BoxSet.SHATTERED_TIMELINES),
    VillainInsert(
        Villain.kismet, BoxSet.SHATTERED_TIMELINES, AlternateTags.the_unstable
    ),
    VillainInsert(Villain.la_capitan, BoxSet.SHATTERED_TIMELINES),
    VillainInsert(Villain.la_capitan, BoxSet.VILLAINS, AlternateTags.team_villain),
    VillainInsert(
        Villain.matriarch,
        BoxSet.ROOK_CITY,
    ),
    VillainInsert(
        Villain.matriarch, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(
        Villain.matriarch, BoxSet.DEFINITIVE_EDITION, AlternateTags.mocktriarch
    ),
    VillainInsert(Villain.miss_information, BoxSet.MISS_INFORMATION),
    VillainInsert(
        Villain.miss_information, BoxSet.MISS_INFORMATION, AlternateTags.team_villain
    ),
    VillainInsert(Villain.nixious_the_chosen, BoxSet.OBLIVAEON),
    VillainInsert(Villain.oblivaeon, BoxSet.OBLIVAEON),
    VillainInsert(Villain.omnitron, BoxSet.ENHANCED_EDITION),
    VillainInsert(
        Villain.omnitron,
        BoxSet.ENHANCED_EDITION,
        AlternateTags.cosmic,
    ),
    VillainInsert(
        Villain.omnitron, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive
    ),
    VillainInsert(
        Villain.omnitron, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive_cosmic
    ),
    VillainInsert(Villain.the_operative, BoxSet.VILLAINS),
    VillainInsert(Villain.plague_rat, BoxSet.ROOK_CITY),
    VillainInsert(Villain.plague_rat, BoxSet.VILLAINS, AlternateTags.team_villain),
    VillainInsert(Villain.progeny, BoxSet.WRATH_OF_THE_COSMOS),
    VillainInsert(Villain.progeny, BoxSet.OBLIVAEON, AlternateTags.scion),
    VillainInsert(Villain.proletariat, BoxSet.VENGEANCE),
    VillainInsert(
        Villain.sanction,
        BoxSet.OBLIVAEON,
    ),
    VillainInsert(Villain.sergeant_steel, BoxSet.VILLAINS),
    VillainInsert(
        Villain.spite,
        BoxSet.ROOK_CITY,
    ),
    VillainInsert(Villain.spite, BoxSet.ROOK_CITY, AlternateTags.agent_of_gloom),
    VillainInsert(
        Villain.voidsoul,
        BoxSet.OBLIVAEON,
    ),
    VillainInsert(Villain.wager_master, BoxSet.WAGER_MASTER),
    VillainInsert(Villain.anathema, BoxSet.CAULDRON),
    VillainInsert(Villain.anathema, BoxSet.CAULDRON, AlternateTags.evolved),
    VillainInsert(Villain.dendron, BoxSet.CAULDRON),
    VillainInsert(Villain.dendron, BoxSet.CAULDRON, AlternateTags.windcolor),
    VillainInsert(Villain.gray, BoxSet.CAULDRON),
    VillainInsert(Villain.the_ram, BoxSet.CAULDRON),
    VillainInsert(Villain.the_ram, BoxSet.CAULDRON, AlternateTags.alt_1929),
    VillainInsert(Villain.tiamat, BoxSet.CAULDRON),
    VillainInsert(Villain.tiamat, BoxSet.CAULDRON, AlternateTags.hydra),
    VillainInsert(Villain.oriphel, BoxSet.CAULDRON_EXPERIMENTAL),
    VillainInsert(Villain.swarm_eater, BoxSet.CAULDRON_EXPERIMENTAL),
    VillainInsert(
        Villain.swarm_eater, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.hivemind
    ),
    VillainInsert(Villain.vector, BoxSet.CAULDRON_EXPERIMENTAL),
    VillainInsert(Villain.phase, BoxSet.CAULDRON_STORMFALL),
    VillainInsert(Villain.celadroch, BoxSet.CAULDRON_STORMFALL),
    VillainInsert(Villain.menagerie, BoxSet.CAULDRON_STORMFALL),
    VillainInsert(Villain.infernal_choir, BoxSet.CAULDRON_ADRIFT),
    VillainInsert(Villain.mistress_of_fate, BoxSet.CAULDRON_ADRIFT),
    VillainInsert(Villain.mythos, BoxSet.CAULDRON_ADRIFT),
    VillainInsert(Villain.outlander, BoxSet.CAULDRON_ADRIFT),
    VillainInsert(Villain.screamachine, BoxSet.CAULDRON_ADRIFT),
]
