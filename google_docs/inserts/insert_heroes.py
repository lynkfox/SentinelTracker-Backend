from dataclasses import dataclass, field
from common.models.character_enums import (
    AlternateTags,
    Hero,
    HERO_DISPLAY_MAPPING,
    ALTERNATE_TAG_DISPLAY_MAPPING,
)
from common.models.game_details_enums import BoxSet
from typing import Union


@dataclass
class HeroInsert:
    character: Union[Hero, str]
    box_set: Union[BoxSet, str]
    alternate_name: Union[AlternateTags, str, None] = field(default=None)
    base: Union[Hero, str] = field(default=None)
    full_name: str = field(init=False)
    query_name_value: str = field(init=False)
    query_alt_value: str = field(init=False)

    def __post_init__(self):

        display_name = HERO_DISPLAY_MAPPING.get(self.character)
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

        self.box_set = self.box_set.value
        self.base = display_name

        if self.alternate_name is not None and is_definitive:
            self.full_name = f"{display_name}{ALTERNATE_TAG_DISPLAY_MAPPING.get(AlternateTags.definitive)}{display_alt}"
        elif self.alternate_name is not None:
            self.full_name = f"{display_name}{display_alt}"
        else:
            self.full_name = display_name


def _deal_with_alt_prefix(name: str):
    key = "alt_"
    if name.startswith(key):
        return name.replace(key, "")

    else:
        return name


HEROES_TO_INSERT = [
    HeroInsert(Hero.absolute_zero, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.absolute_zero, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_five),
    HeroInsert(Hero.absolute_zero, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_six),
    HeroInsert(Hero.absolute_zero, BoxSet.ENHANCED_EDITION, AlternateTags.termi_nation),
    HeroInsert(Hero.absolute_zero, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.absolute_zero, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.akash_thriya, BoxSet.OBLIVAEON),
    HeroInsert(Hero.akash_thriya, BoxSet.OBLIVAEON, AlternateTags.spirit_of_the_void),
    HeroInsert(Hero.argent_adept, BoxSet.INFERNAL_RELICS),
    HeroInsert(Hero.argent_adept, BoxSet.INFERNAL_RELICS, AlternateTags.prime_wardens),
    HeroInsert(Hero.argent_adept, BoxSet.INFERNAL_RELICS, AlternateTags.dark_conductor),
    HeroInsert(Hero.argent_adept, BoxSet.INFERNAL_RELICS, AlternateTags.xtreme_prime_wardens),
    HeroInsert(Hero.argent_adept, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.argent_adept, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.bench_mark, BoxSet.BENCHMARK),
    HeroInsert(Hero.bench_mark, BoxSet.BENCHMARK, AlternateTags.supply_and_demand),
    HeroInsert(Hero.bunker, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.bunker, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_five),
    HeroInsert(Hero.bunker, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_six),
    HeroInsert(Hero.bunker, BoxSet.ENHANCED_EDITION, AlternateTags.gi),
    HeroInsert(Hero.bunker, BoxSet.ENHANCED_EDITION, AlternateTags.termi_nation),
    HeroInsert(Hero.bunker, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.bunker, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.captain_cosmic, BoxSet.WRATH_OF_THE_COSMOS),
    HeroInsert(Hero.captain_cosmic, BoxSet.WRATH_OF_THE_COSMOS, AlternateTags.prime_wardens),
    HeroInsert(
        Hero.captain_cosmic,
        BoxSet.WRATH_OF_THE_COSMOS,
        AlternateTags.xtreme_prime_wardens,
    ),
    HeroInsert(Hero.captain_cosmic, BoxSet.WRATH_OF_THE_COSMOS, AlternateTags.requital),
    HeroInsert(Hero.captain_cosmic, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.captain_cosmic, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.chrono_ranger, BoxSet.SHATTERED_TIMELINES),
    HeroInsert(Hero.chrono_ranger, BoxSet.SHATTERED_TIMELINES, AlternateTags.best_of_times),
    HeroInsert(Hero.doctor_medico, BoxSet.VOID_GUARD),
    HeroInsert(Hero.doctor_medico, BoxSet.VOID_GUARD, AlternateTags.malpractice),
    HeroInsert(Hero.expatriette, BoxSet.ROOK_CITY),
    HeroInsert(Hero.expatriette, BoxSet.ROOK_CITY, AlternateTags.dark_watch),
    HeroInsert(Hero.fanatic, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.fanatic, BoxSet.ENHANCED_EDITION, AlternateTags.redeemer),
    HeroInsert(Hero.fanatic, BoxSet.ENHANCED_EDITION, AlternateTags.prime_wardens),
    HeroInsert(Hero.fanatic, BoxSet.ENHANCED_EDITION, AlternateTags.xtreme_prime_wardens),
    HeroInsert(Hero.fanatic, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.fanatic, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.guise, BoxSet.GUISE),
    HeroInsert(Hero.guise, BoxSet.GUISE, AlternateTags.santa),
    HeroInsert(Hero.guise, BoxSet.GUISE, AlternateTags.completionist),
    HeroInsert(Hero.haka, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.haka, BoxSet.ENHANCED_EDITION, AlternateTags.prime_wardens),
    HeroInsert(Hero.haka, BoxSet.ENHANCED_EDITION, AlternateTags.xtreme_prime_wardens),
    HeroInsert(Hero.haka, BoxSet.ENHANCED_EDITION, AlternateTags.eternal),
    HeroInsert(Hero.haka, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.haka, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.harpy, BoxSet.OBLIVAEON),
    HeroInsert(Hero.harpy, BoxSet.OBLIVAEON, AlternateTags.dark_watch),
    HeroInsert(Hero.idealist, BoxSet.VOID_GUARD),
    HeroInsert(Hero.idealist, BoxSet.VOID_GUARD, AlternateTags.super_sentai),
    HeroInsert(Hero.knyfe, BoxSet.VENGEANCE),
    HeroInsert(Hero.knyfe, BoxSet.VENGEANCE, AlternateTags.rogue_agent),
    HeroInsert(Hero.la_comodora, BoxSet.OBLIVAEON),
    HeroInsert(Hero.la_comodora, BoxSet.OBLIVAEON, AlternateTags.curse_of_the_black_spot),
    HeroInsert(Hero.legacy, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.legacy, BoxSet.ENHANCED_EDITION, AlternateTags.americas_greatest),
    HeroInsert(Hero.legacy, BoxSet.ENHANCED_EDITION, AlternateTags.americas_newest),
    HeroInsert(Hero.legacy, BoxSet.ENHANCED_EDITION, AlternateTags.americas_cleverest),
    HeroInsert(Hero.legacy, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_five),
    HeroInsert(Hero.legacy, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.legacy, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.lifeline, BoxSet.OBLIVAEON),
    HeroInsert(Hero.lifeline, BoxSet.OBLIVAEON, AlternateTags.bloodmage),
    HeroInsert(Hero.luminary, BoxSet.OBLIVAEON),
    HeroInsert(Hero.luminary, BoxSet.OBLIVAEON, AlternateTags.heroic),
    HeroInsert(Hero.mainstay, BoxSet.VOID_GUARD),
    HeroInsert(Hero.mainstay, BoxSet.VOID_GUARD, AlternateTags.road_warrior),
    HeroInsert(Hero.mr_fixer, BoxSet.ROOK_CITY),
    HeroInsert(Hero.mr_fixer, BoxSet.ROOK_CITY, AlternateTags.dark_watch),
    HeroInsert(Hero.naturalist, BoxSet.VENGEANCE),
    HeroInsert(Hero.naturalist, BoxSet.VENGEANCE, AlternateTags.the_hunted),
    HeroInsert(Hero.nightmist, BoxSet.INFERNAL_RELICS),
    HeroInsert(Hero.nightmist, BoxSet.INFERNAL_RELICS, AlternateTags.dark_watch),
    HeroInsert(Hero.ominitron_x, BoxSet.SHATTERED_TIMELINES),
    HeroInsert(Hero.ominitron_x, BoxSet.SHATTERED_TIMELINES, AlternateTags.u),
    HeroInsert(
        Hero.parse,
        BoxSet.VENGEANCE,
    ),
    HeroInsert(Hero.parse, BoxSet.VENGEANCE, AlternateTags.fugue_state),
    HeroInsert(Hero.ra, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.ra, BoxSet.ENHANCED_EDITION, AlternateTags.horus_of_the_two_horizon),
    HeroInsert(Hero.ra, BoxSet.ENHANCED_EDITION, AlternateTags.setting_sun),
    HeroInsert(Hero.ra, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.ra, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.scholar, BoxSet.SCHOLAR),
    HeroInsert(Hero.scholar, BoxSet.SCHOLAR, AlternateTags.of_the_infinite),
    HeroInsert(Hero.setback, BoxSet.VENGEANCE),
    HeroInsert(Hero.setback, BoxSet.VENGEANCE, AlternateTags.dark_watch),
    HeroInsert(
        Hero.sky_scraper,
        BoxSet.WRATH_OF_THE_COSMOS,
    ),
    HeroInsert(Hero.sky_scraper, BoxSet.WRATH_OF_THE_COSMOS, AlternateTags.extremist),
    HeroInsert(Hero.southwest_sentinels, BoxSet.VENGEANCE),
    HeroInsert(Hero.southwest_sentinels, BoxSet.VENGEANCE, AlternateTags.adamant),
    HeroInsert(Hero.stuntman, BoxSet.STUNTMAN),
    HeroInsert(Hero.stuntman, BoxSet.STUNTMAN, AlternateTags.action_hero),
    HeroInsert(Hero.tachyon, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.tachyon, BoxSet.ENHANCED_EDITION, AlternateTags.super_scientific),
    HeroInsert(Hero.tachyon, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_five),
    HeroInsert(Hero.tachyon, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_six),
    HeroInsert(Hero.tachyon, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.tachyon, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.tempest, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.tempest, BoxSet.ENHANCED_EDITION, AlternateTags.prime_wardens),
    HeroInsert(Hero.tempest, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_six),
    HeroInsert(Hero.tempest, BoxSet.ENHANCED_EDITION, AlternateTags.xtreme_prime_wardens),
    HeroInsert(Hero.tempest, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.tempest, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.unity, BoxSet.UNITY),
    HeroInsert(Hero.unity, BoxSet.UNITY, AlternateTags.termi_nation),
    HeroInsert(Hero.unity, BoxSet.UNITY, AlternateTags.freedom_six),
    HeroInsert(Hero.unity, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.unity, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.visionary, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.visionary, BoxSet.ENHANCED_EDITION, AlternateTags.dark),
    HeroInsert(Hero.visionary, BoxSet.ENHANCED_EDITION, AlternateTags.unleashed),
    HeroInsert(Hero.wraith, BoxSet.ENHANCED_EDITION),
    HeroInsert(Hero.wraith, BoxSet.ENHANCED_EDITION, AlternateTags.rook_city),
    HeroInsert(Hero.wraith, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_five),
    HeroInsert(Hero.wraith, BoxSet.ENHANCED_EDITION, AlternateTags.freedom_six),
    HeroInsert(Hero.wraith, BoxSet.DEFINITIVE_EDITION, AlternateTags.definitive),
    HeroInsert(Hero.wraith, BoxSet.DEFINITIVE_EDITION, AlternateTags.first_appearance),
    HeroInsert(Hero.writhe, BoxSet.VOID_GUARD),
    HeroInsert(Hero.writhe, BoxSet.VOID_GUARD, AlternateTags.cosmic_inventor),
    HeroInsert(Hero.baccarat, BoxSet.CAULDRON),
    HeroInsert(Hero.baccarat, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.baccarat, BoxSet.CAULDRON, AlternateTags.ace_of_sorrows),
    HeroInsert(Hero.baccarat, BoxSet.CAULDRON, AlternateTags.ace_of_swords),
    HeroInsert(Hero.doc_havoc, BoxSet.CAULDRON),
    HeroInsert(Hero.doc_havoc, BoxSet.CAULDRON, AlternateTags.alt_2199),
    HeroInsert(Hero.doc_havoc, BoxSet.CAULDRON, AlternateTags.first_response),
    HeroInsert(Hero.the_knight, BoxSet.CAULDRON),
    HeroInsert(Hero.the_knight, BoxSet.CAULDRON, AlternateTags.the_berserker),
    HeroInsert(Hero.the_knight, BoxSet.CAULDRON, AlternateTags.the_fair),
    HeroInsert(Hero.the_knight, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.the_knight, BoxSet.CAULDRON, AlternateTags.wasteland_ronin),
    HeroInsert(Hero.lady_of_the_wood, BoxSet.CAULDRON),
    HeroInsert(Hero.lady_of_the_wood, BoxSet.CAULDRON, AlternateTags.alt_2199),
    HeroInsert(
        Hero.lady_of_the_wood,
        BoxSet.CAULDRON,
        AlternateTags.ministry_of_strategic_science,
    ),
    HeroInsert(Hero.lady_of_the_wood, BoxSet.CAULDRON, AlternateTags.season_of_change),
    HeroInsert(Hero.malichae, BoxSet.CAULDRON),
    HeroInsert(Hero.malichae, BoxSet.CAULDRON, AlternateTags.ministry_of_strategic_science),
    HeroInsert(Hero.malichae, BoxSet.CAULDRON, AlternateTags.shardmaster),
    HeroInsert(Hero.necro, BoxSet.CAULDRON),
    HeroInsert(Hero.necro, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.necro, BoxSet.CAULDRON, AlternateTags.warden_of_chaos),
    HeroInsert(Hero.quicksilver, BoxSet.CAULDRON),
    HeroInsert(Hero.quicksilver, BoxSet.CAULDRON, AlternateTags.the_uncanny),
    HeroInsert(Hero.quicksilver, BoxSet.CAULDRON, AlternateTags.renegade),
    HeroInsert(Hero.starlight, BoxSet.CAULDRON),
    HeroInsert(Hero.starlight, BoxSet.CAULDRON, AlternateTags.genesis),
    HeroInsert(Hero.starlight, BoxSet.CAULDRON, AlternateTags.nightlore_council),
    HeroInsert(Hero.the_stranger, BoxSet.CAULDRON),
    HeroInsert(Hero.the_stranger, BoxSet.CAULDRON, AlternateTags.the_rune_carved),
    HeroInsert(Hero.the_stranger, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.the_stranger, BoxSet.CAULDRON, AlternateTags.wasteland_ronin),
    HeroInsert(Hero.tango_one, BoxSet.CAULDRON),
    HeroInsert(Hero.tango_one, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.tango_one, BoxSet.CAULDRON, AlternateTags.ghost_ops),
    HeroInsert(Hero.vanish, BoxSet.CAULDRON),
    HeroInsert(Hero.vanish, BoxSet.CAULDRON, AlternateTags.alt_1929),
    HeroInsert(Hero.vanish, BoxSet.CAULDRON, AlternateTags.first_response),
    HeroInsert(Hero.cricket, BoxSet.CAULDRON_EXPERIMENTAL),
    HeroInsert(Hero.cricket, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.first_response),
    HeroInsert(Hero.cricket, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.renegade),
    HeroInsert(Hero.cricket, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.wasteland_ronin),
    HeroInsert(Hero.cypher, BoxSet.CAULDRON_EXPERIMENTAL),
    HeroInsert(Hero.cypher, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.first_response),
    HeroInsert(Hero.cypher, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.swarming_protocol),
    HeroInsert(Hero.titan, BoxSet.CAULDRON_EXPERIMENTAL),
    HeroInsert(Hero.titan, BoxSet.CAULDRON_EXPERIMENTAL, AlternateTags.alt_2199),
    HeroInsert(
        Hero.titan,
        BoxSet.CAULDRON_EXPERIMENTAL,
        AlternateTags.ministry_of_strategic_science,
    ),
    HeroInsert(Hero.echelon, BoxSet.CAULDRON_STORMFALL),
    HeroInsert(Hero.echelon, BoxSet.CAULDRON_STORMFALL, AlternateTags.alt_2199),
    HeroInsert(Hero.echelon, BoxSet.CAULDRON_STORMFALL, AlternateTags.first_response),
    HeroInsert(Hero.impact, BoxSet.CAULDRON_STORMFALL),
    HeroInsert(Hero.impact, BoxSet.CAULDRON_STORMFALL, AlternateTags.renegade),
    HeroInsert(Hero.impact, BoxSet.CAULDRON_STORMFALL, AlternateTags.wasteland_ronin),
    HeroInsert(Hero.magnificent_mara, BoxSet.CAULDRON_STORMFALL),
    HeroInsert(Hero.magnificent_mara, BoxSet.CAULDRON_STORMFALL, AlternateTags.alt_1929),
    HeroInsert(
        Hero.magnificent_mara,
        BoxSet.CAULDRON_STORMFALL,
        AlternateTags.ministry_of_strategic_science,
    ),
    HeroInsert(Hero.drift, BoxSet.CAULDRON_ADRIFT),
    HeroInsert(Hero.drift, BoxSet.CAULDRON_ADRIFT, AlternateTags.alt_1929_2199),
    HeroInsert(Hero.drift, BoxSet.CAULDRON_ADRIFT, AlternateTags.through_the_breach),
    HeroInsert(Hero.gargoyle, BoxSet.CAULDRON_ADRIFT),
    HeroInsert(Hero.gargoyle, BoxSet.CAULDRON_ADRIFT, AlternateTags.alt_2199),
    HeroInsert(Hero.gargoyle, BoxSet.CAULDRON_ADRIFT, AlternateTags.wasteland_ronin),
    HeroInsert(Hero.gyrosaur, BoxSet.CAULDRON_ADRIFT),
    HeroInsert(Hero.gyrosaur, BoxSet.CAULDRON_ADRIFT, AlternateTags.renegade),
    HeroInsert(Hero.gyrosaur, BoxSet.CAULDRON_ADRIFT, AlternateTags.speed_demon),
]
