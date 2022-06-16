from google_docs.inserts.insert_environments import EnvironmentInsert
from google_docs.inserts.insert_heroes import HeroInsert
from google_docs.inserts.insert_villains import VillainInsert

from common.models.character_enums import AlternateTags, Hero, Villain, Location
from common.models.game_details_enums import BoxSet


RENEGADE_HERO_INSERTS = [
    HeroInsert(
        Hero.expatriette,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.expatriette,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.expatriette,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.dark_watch,
    ),
    HeroInsert(
        Hero.expatriette,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.eclipse,
    ),
    HeroInsert(
        Hero.setback,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.setback,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.setback,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.dark_watch,
    ),
    HeroInsert(
        Hero.setback,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.fey_cursed,
    ),
    HeroInsert(
        Hero.mr_fixer,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.mr_fixer,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.mr_fixer,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.dark_watch,
    ),
    HeroInsert(
        Hero.mr_fixer,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.blackfist,
    ),
    HeroInsert(
        Hero.nightmist,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.nightmist,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.nightmist,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.dark_watch,
    ),
    HeroInsert(
        Hero.nightmist,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.mentor,
    ),
    HeroInsert(
        Hero.harpy,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.harpy,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.harpy,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.dark_watch,
    ),
    HeroInsert(
        Hero.harpy,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.blood_raven,
    ),
    HeroInsert(
        Hero.alpha,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    HeroInsert(
        Hero.alpha,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.first_appearance,
    ),
    HeroInsert(
        Hero.alpha,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.reporter,
    ),
    HeroInsert(
        Hero.alpha,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.alt_2000,
    ),
    HeroInsert(
        Hero.wraith,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.detective,
    ),
    HeroInsert(
        Hero.unity,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.scavanger,
    ),
    HeroInsert(
        Hero.bunker,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.stealth_suit,
    ),
    HeroInsert(
        Hero.fanatic,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.haunted,
    ),
    HeroInsert(
        Hero.ra,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.backdraft,
    ),
    HeroInsert(
        Hero.haka,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.werewolf,
    ),
]

RENEGADE_VILLAIN_INSERTS = [
    VillainInsert(
        Villain.the_organization,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.the_organization,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.bear,
    ),
    VillainInsert(
        Villain.plague_rat,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.plague_rat,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.doctor_toxica,
    ),
    VillainInsert(
        Villain.spite,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.spite,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.abomination,
    ),
    VillainInsert(
        Villain.gloomweaver,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.gloomweaver,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.soultaker,
    ),
    VillainInsert(
        Villain.kismet,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.kismet,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.empowered,
    ),
    VillainInsert(
        Villain.ambuscade,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.ambuscade,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.vainglorious,
    ),
    VillainInsert(
        Villain.apex,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.apex,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.blood_leashed,
    ),
    VillainInsert(
        Villain.fey_court,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.fey_court,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.war_girded,
    ),
    VillainInsert(
        Villain.terraform,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    VillainInsert(
        Villain.terraform,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.mark_iii,
    ),
]

RENEGADE_ENVIRONMENT_INSERTS = [
    EnvironmentInsert(
        Location.diamond_manor,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(
        Location.pike_industrial_complex,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(
        Location.rook_city,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(
        Location.realm_of_discord,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
    EnvironmentInsert(
        Location.temple_of_zhu_long,
        BoxSet.ROOK_CITY_RENEGADES,
        AlternateTags.definitive,
    ),
]
