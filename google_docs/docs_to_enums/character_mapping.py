from common.models.game_details_enums import (
    HeroWinCondition,
    HeroLossCondition,
    SelectionMethod,
    Platform,
    GameLength,
)
from common.models.character_enums import (
    Villain,
    Hero,
    Environment,
    AlternateTags,
    VILLAIN_DISPLAY_MAPPING,
    HERO_DISPLAY_MAPPING,
    ENVIRONMENT_DISPLAY_MAPPING,
)
from common.rds import character_full_name


ENVIRONMENT_GOOGLE_TO_RDS_MAP = {
    "Celestial Tribunal": character_full_name(
        Environment.celestial_tribunal, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Champion Studios": character_full_name(
        Environment.champion_studios, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Dok'Thorath": character_full_name(
        Environment.dok_thorath_capital, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Enclave of the Endlings": character_full_name(
        Environment.enclave_of_the_endlings, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Fort Adamant": character_full_name(
        Environment.fort_adamant, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Freedom Tower": character_full_name(
        Environment.freedom_tower, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Insula Primalis": character_full_name(
        Environment.insula_primalis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Madame Mittermeier's": character_full_name(
        Environment.madame_mittermeiers, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Maerynian Refuge": character_full_name(
        Environment.maerynian_refuge, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Magmaria": character_full_name(
        Environment.magmaria, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Megalopolis": character_full_name(
        Environment.megalopolis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Mobile Defense Platform": character_full_name(
        Environment.mobile_defense_platform, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Mordengrad": character_full_name(
        Environment.mordengrad, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Nexus of the Void": character_full_name(
        Environment.nexus_of_the_void, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Omnitron IV": character_full_name(
        Environment.omnitron_iv, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Pike Industrial Complex": character_full_name(
        Environment.pike_industrial_complex, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Realm of Discord": character_full_name(
        Environment.realm_of_discord, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Rook City": character_full_name(
        Environment.rook_city, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Ruins of Atlantis": character_full_name(
        Environment.ruins_of_atlantis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Silver Gulch 1883": character_full_name(
        Environment.silver_gulch_1883, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Temple of Zhu Long": character_full_name(
        Environment.temple_of_zhu_long, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Block": character_full_name(
        Environment.the_block, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Court of Blood": character_full_name(
        Environment.court_of_blood, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Final Wasteland": character_full_name(
        Environment.the_final_wasteland, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Time Cataclysm": character_full_name(
        Environment.time_cataclysm, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Tomb of Anubis": character_full_name(
        Environment.tomb_of_anubis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Wagner Mars Base": character_full_name(
        Environment.wagner_mars_base, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
}

VILLAIN_GOOGLE_TO_RDS_MAP = {
    "(None)": None,
    "Agent of Gloom Spite": character_full_name(
        Villain.spite, AlternateTags.agent_of_gloom, VILLAIN_DISPLAY_MAPPING
    ),
    "Akash'bhuta": character_full_name(
        Villain.akash_bhuta, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Ambuscade": character_full_name(Villain.ambuscade, None, VILLAIN_DISPLAY_MAPPING),
    "Ambuscade (Vengeance)": character_full_name(
        Villain.ambuscade, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Apostate": character_full_name(Villain.apostate, None, VILLAIN_DISPLAY_MAPPING),
    "Baron Blade": character_full_name(
        Villain.baron_blade, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Baron Blade (Vengeance)": character_full_name(
        Villain.baron_blade, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Biomancer (Vengeance)": character_full_name(
        Villain.biomancer, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Bugbear (Vengeance)": character_full_name(
        Villain.bugbear, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Chokepoint": character_full_name(
        Villain.chokepoint, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Citizen Dawn": character_full_name(
        Villain.citizen_dawn, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Citizens Hammer and Anvil (Vengeance)": character_full_name(
        Villain.citizens_hammer_and_anvil, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Cosmic Omnitron": character_full_name(
        Villain.omnitron, AlternateTags.cosmic, VILLAIN_DISPLAY_MAPPING
    ),
    "Deadline": character_full_name(Villain.deadline, None, VILLAIN_DISPLAY_MAPPING),
    "Ermine (Vengeance)": character_full_name(
        Villain.ermine, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Friction (Vengeance)": character_full_name(
        Villain.friction, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Fright Train (Vengeance)": character_full_name(
        Villain.fright_train, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Gloomweaver": character_full_name(
        Villain.gloomweaver, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Grand Warlord Voss": character_full_name(
        Villain.grand_warlord_voss, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Greazer Clutch (Vengeance)": character_full_name(
        Villain.greazer_clutch, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Infinitor": character_full_name(Villain.infinitor, None, VILLAIN_DISPLAY_MAPPING),
    "Iron Legacy": character_full_name(
        Villain.iron_legacy, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Kaargra Warfang": character_full_name(
        Villain.kaargra_warfang, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Kismet": character_full_name(Villain.kismet, None, VILLAIN_DISPLAY_MAPPING),
    "La Capitan": character_full_name(
        Villain.la_capitan, None, VILLAIN_DISPLAY_MAPPING
    ),
    "La Capitan (Vengeance)": character_full_name(
        Villain.la_capitan, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Mad Bomber Blade": character_full_name(
        Villain.baron_blade, AlternateTags.mad_bomber, VILLAIN_DISPLAY_MAPPING
    ),
    "Miss Information": character_full_name(
        Villain.miss_information, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Miss Information (Vengeance)": character_full_name(
        Villain.miss_information, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Omnitron": character_full_name(Villain.omnitron, None, VILLAIN_DISPLAY_MAPPING),
    "Plague Rat": character_full_name(
        Villain.plague_rat, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Plague Rat (Vengeance)": character_full_name(
        Villain.plague_rat, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Progeny": character_full_name(Villain.progeny, None, VILLAIN_DISPLAY_MAPPING),
    "Proletariat (Vengeance)": character_full_name(
        Villain.proletariat, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Sergeant Steel (Vengeance)": character_full_name(
        Villain.sergeant_steel, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Skinwalker Gloomweaver": character_full_name(
        Villain.gloomweaver, AlternateTags.skinwalker, VILLAIN_DISPLAY_MAPPING
    ),
    "Spite": character_full_name(Villain.spite, None, VILLAIN_DISPLAY_MAPPING),
    "The Chairman": character_full_name(
        Villain.chairman, None, VILLAIN_DISPLAY_MAPPING
    ),
    "The Dreamer": character_full_name(
        Villain.the_dreamer, None, VILLAIN_DISPLAY_MAPPING
    ),
    "The Ennead": character_full_name(
        Villain.the_ennead, None, VILLAIN_DISPLAY_MAPPING
    ),
    "The Matriarch": character_full_name(
        Villain.matriarch, None, VILLAIN_DISPLAY_MAPPING
    ),
    "The Operative (Vengeance)": character_full_name(
        Villain.the_operative, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Tormented Infinitor": character_full_name(
        Villain.infinitor, AlternateTags.heroic, VILLAIN_DISPLAY_MAPPING
    ),
    "Unstable Kismet": character_full_name(
        Villain.kismet, AlternateTags.the_unstable, VILLAIN_DISPLAY_MAPPING
    ),
    "Vengeance Five": None,
    "Vengeance Style (Vengeance and Villains)": None,
    "Wager Master": character_full_name(
        Villain.wager_master, None, VILLAIN_DISPLAY_MAPPING
    ),
}

HERO_GOOGLE_TO_RDS_MAPPING = {
    "(None - Selecting this option here will remove your entry from the general statistics, but provide us with interesting stats for 2 hero games in a separate study)": None,
    "(none)": None,
    "(None)": None,
    "Absolute Zero": character_full_name(
        Hero.absolute_zero, None, HERO_DISPLAY_MAPPING
    ),
    "Absolute Zero: Freedom Five": character_full_name(
        Hero.absolute_zero, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Absolute Zero: Freedom Six (Elemental Wrath)": character_full_name(
        Hero.absolute_zero, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Absolute Zero: Termi-Nation": character_full_name(
        Hero.absolute_zero, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Akash'Thriya": character_full_name(Hero.akash_thriya, None, HERO_DISPLAY_MAPPING),
    "Akash'Thriya: Spirit of the Void": character_full_name(
        Hero.akash_thriya, AlternateTags.spirit_of_the_void, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept": character_full_name(Hero.argent_adept, None, HERO_DISPLAY_MAPPING),
    "Argent Adept: Dark Conductor (Kvothe)": character_full_name(
        Hero.argent_adept, AlternateTags.dark_conductor, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept: Prime Warden": character_full_name(
        Hero.argent_adept, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept: XTREME Prime Warden": character_full_name(
        Hero.argent_adept, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Benchmark": character_full_name(Hero.bench_mark, None, HERO_DISPLAY_MAPPING),
    "Benchmark: Supply and Demand": character_full_name(
        Hero.bench_mark, AlternateTags.supply_and_demand, HERO_DISPLAY_MAPPING
    ),
    "Bunker": character_full_name(Hero.bunker, None, HERO_DISPLAY_MAPPING),
    "Bunker: Freedom Five": character_full_name(
        Hero.bunker, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Bunker: Freedom Six (Engine of War)": character_full_name(
        Hero.bunker, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Bunker: GI": character_full_name(
        Hero.bunker, AlternateTags.gi, HERO_DISPLAY_MAPPING
    ),
    "Bunker: Termi-Nation": character_full_name(
        Hero.bunker, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic": character_full_name(
        Hero.captain_cosmic, None, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic: Prime Warden": character_full_name(
        Hero.captain_cosmic, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic: Requital": character_full_name(
        Hero.captain_cosmic, AlternateTags.requital, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic: XTREME Prime Warden": character_full_name(
        Hero.captain_cosmic, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Chrono-Ranger": character_full_name(
        Hero.chrono_ranger, None, HERO_DISPLAY_MAPPING
    ),
    "Chrono-Ranger: Best of Times": character_full_name(
        Hero.chrono_ranger, AlternateTags.best_of_times, HERO_DISPLAY_MAPPING
    ),
    "Dr. Medico: Void Guard": character_full_name(
        Hero.doctor_medico, None, HERO_DISPLAY_MAPPING
    ),
    "Dr. Medico: Void Guard, Malpractice": character_full_name(
        Hero.doctor_medico, AlternateTags.malpractice, HERO_DISPLAY_MAPPING
    ),
    "Expatriette": character_full_name(Hero.expatriette, None, HERO_DISPLAY_MAPPING),
    "Expatriette: Dark Watch": character_full_name(
        Hero.expatriette, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Fanatic": character_full_name(Hero.fanatic, None, HERO_DISPLAY_MAPPING),
    "Fanatic: Prime Warden": character_full_name(
        Hero.fanatic, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Fanatic: Redeemer": character_full_name(
        Hero.fanatic, AlternateTags.redeemer, HERO_DISPLAY_MAPPING
    ),
    "Fanatic: XTREME Prime Warden": character_full_name(
        Hero.fanatic, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Guise": character_full_name(Hero.guise, None, HERO_DISPLAY_MAPPING),
    "Guise: Completionist": character_full_name(
        Hero.guise, AlternateTags.completionist, HERO_DISPLAY_MAPPING
    ),
    "Guise: Santa": character_full_name(
        Hero.guise, AlternateTags.santa, HERO_DISPLAY_MAPPING
    ),
    "Haka": character_full_name(Hero.haka, None, HERO_DISPLAY_MAPPING),
    "Haka: Eternal": character_full_name(
        Hero.haka, AlternateTags.eternal, HERO_DISPLAY_MAPPING
    ),
    "Haka: Prime Warden": character_full_name(
        Hero.haka, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Haka: XTREME Prime Warden": character_full_name(
        Hero.haka, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Harpy": character_full_name(Hero.harpy, None, HERO_DISPLAY_MAPPING),
    "Harpy: Dark Watch": character_full_name(
        Hero.harpy, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Idealist: Void Guard": character_full_name(
        Hero.idealist, None, HERO_DISPLAY_MAPPING
    ),
    "Idealist: Void Guard, Super Sentai": character_full_name(
        Hero.idealist, AlternateTags.super_sentai, HERO_DISPLAY_MAPPING
    ),
    "K.N.Y.F.E.": character_full_name(Hero.knyfe, None, HERO_DISPLAY_MAPPING),
    "K.N.Y.F.E.: Rogue Agent": character_full_name(
        Hero.knyfe, AlternateTags.rogue_agent, HERO_DISPLAY_MAPPING
    ),
    "La Comodora": character_full_name(Hero.la_comodora, None, HERO_DISPLAY_MAPPING),
    "La Comodora: Curse of the Black Spot": character_full_name(
        Hero.la_comodora, AlternateTags.curse_of_the_black_spot, HERO_DISPLAY_MAPPING
    ),
    "Legacy": character_full_name(Hero.legacy, None, HERO_DISPLAY_MAPPING),
    "Legacy: Freedom Five": character_full_name(
        Hero.legacy, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Legacy: Greatest": character_full_name(
        Hero.legacy, AlternateTags.americas_greatest, HERO_DISPLAY_MAPPING
    ),
    "Legacy: Young": character_full_name(
        Hero.legacy, AlternateTags.americas_newest, HERO_DISPLAY_MAPPING
    ),
    "Lifeline": character_full_name(Hero.lifeline, None, HERO_DISPLAY_MAPPING),
    "Lifeline: Blood Mage": character_full_name(
        Hero.lifeline, AlternateTags.bloodmage, HERO_DISPLAY_MAPPING
    ),
    "Luminary": character_full_name(Hero.luminary, None, HERO_DISPLAY_MAPPING),
    "Luminary: Heroic (Ivana)": character_full_name(
        Hero.luminary, AlternateTags.heroic, HERO_DISPLAY_MAPPING
    ),
    "Mainstay: Void Guard": character_full_name(
        Hero.mainstay, None, HERO_DISPLAY_MAPPING
    ),
    "Mainstay: Void Guard, Road Warrior": character_full_name(
        Hero.mainstay, AlternateTags.road_warrior, HERO_DISPLAY_MAPPING
    ),
    "Mr. Fixer": character_full_name(Hero.mr_fixer, None, HERO_DISPLAY_MAPPING),
    "Mr. Fixer: Dark Watch": character_full_name(
        Hero.mr_fixer, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Naturalist": character_full_name(Hero.naturalist, None, HERO_DISPLAY_MAPPING),
    "Naturalist: Hunted": character_full_name(
        Hero.naturalist, AlternateTags.the_hunted, HERO_DISPLAY_MAPPING
    ),
    "Nightmist": character_full_name(Hero.nightmist, None, HERO_DISPLAY_MAPPING),
    "Nightmist: Dark Watch": character_full_name(
        Hero.nightmist, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Omnitron-X": character_full_name(Hero.ominitron_x, None, HERO_DISPLAY_MAPPING),
    "Omnitron-X: Omnitron-U": character_full_name(
        Hero.ominitron_x, AlternateTags.u, HERO_DISPLAY_MAPPING
    ),
    "Parse": character_full_name(Hero.parse, None, HERO_DISPLAY_MAPPING),
    "Parse: Fugue State": character_full_name(
        Hero.parse, AlternateTags.fugue_state, HERO_DISPLAY_MAPPING
    ),
    "Ra": character_full_name(Hero.ra, None, HERO_DISPLAY_MAPPING),
    "Ra: Horus of Two Horizons": character_full_name(
        Hero.ra, AlternateTags.horus_of_the_two_horizon, HERO_DISPLAY_MAPPING
    ),
    "Ra: Setting Sun": character_full_name(
        Hero.ra, AlternateTags.setting_sun, HERO_DISPLAY_MAPPING
    ),
    "Scholar": character_full_name(Hero.scholar, None, HERO_DISPLAY_MAPPING),
    "Scholar: Of the Infinite": character_full_name(
        Hero.scholar, AlternateTags.of_the_infinite, HERO_DISPLAY_MAPPING
    ),
    "Setback": character_full_name(Hero.setback, None, HERO_DISPLAY_MAPPING),
    "Setback: Dark Watch": character_full_name(
        Hero.setback, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Sky-Scraper": character_full_name(Hero.sky_scraper, None, HERO_DISPLAY_MAPPING),
    "Sky-Scraper: Extremist": character_full_name(
        Hero.sky_scraper, AlternateTags.extremist, HERO_DISPLAY_MAPPING
    ),
    "Stuntman": character_full_name(Hero.stuntman, None, HERO_DISPLAY_MAPPING),
    "Stuntman: Action Hero": character_full_name(
        Hero.stuntman, AlternateTags.action_hero, HERO_DISPLAY_MAPPING
    ),
    "Tachyon": character_full_name(Hero.tachyon, None, HERO_DISPLAY_MAPPING),
    "Tachyon: Freedom Five": character_full_name(
        Hero.tachyon, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Tachyon: Freedom Six (Team Leader)": character_full_name(
        Hero.tachyon, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Tachyon: Super Scientific": character_full_name(
        Hero.tachyon, AlternateTags.super_scientific, HERO_DISPLAY_MAPPING
    ),
    "Tempest": character_full_name(Hero.tempest, None, HERO_DISPLAY_MAPPING),
    "Tempest: Freedom Six (Sacrifice)": character_full_name(
        Hero.tempest, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Tempest: Prime Warden": character_full_name(
        Hero.tempest, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Tempest: XTREME Prime Warden": character_full_name(
        Hero.tempest, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "The Sentinels": character_full_name(
        Hero.southwest_sentinels, None, HERO_DISPLAY_MAPPING
    ),
    "The Sentinels: Adamant": character_full_name(
        Hero.southwest_sentinels, AlternateTags.adamant, HERO_DISPLAY_MAPPING
    ),
    "Unity": character_full_name(Hero.unity, None, HERO_DISPLAY_MAPPING),
    "Unity: Freedom Six (Golem)": character_full_name(
        Hero.unity, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Unity: Termi-Nation": character_full_name(
        Hero.unity, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Visionary": character_full_name(Hero.visionary, None, HERO_DISPLAY_MAPPING),
    "Visionary: Dark": character_full_name(
        Hero.visionary, AlternateTags.dark, HERO_DISPLAY_MAPPING
    ),
    "Visionary: Unleashed": character_full_name(
        Hero.visionary, AlternateTags.unleashed, HERO_DISPLAY_MAPPING
    ),
    "Wraith": character_full_name(Hero.wraith, None, HERO_DISPLAY_MAPPING),
    "Wraith: Freedom Five": character_full_name(
        Hero.wraith, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Wraith: Freedom Six (Price of Freedom)": character_full_name(
        Hero.wraith, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Wraith: Rook City": character_full_name(
        Hero.wraith, AlternateTags.rook_city, HERO_DISPLAY_MAPPING
    ),
    "Writhe: Void Guard": character_full_name(Hero.writhe, None, HERO_DISPLAY_MAPPING),
    "Writhe: Void Guard, Cosmic Inventor": character_full_name(
        Hero.writhe, AlternateTags.cosmic_inventor, HERO_DISPLAY_MAPPING
    ),
}

WIN_CONDITION_GOOGLE_TO_RDS = {
    "": HeroWinCondition.STANDARD,
    "Sucker Punch, Final Dive, and other Destroy Cards": HeroWinCondition.STANDARD,
    "Ate Himself (Skinwalker Gloomweaver)": HeroLossCondition.SKINWALKER,
    "Did Not Protect Her (The Dreamer)": HeroLossCondition.DREAMER,
    "Engines Failed (Mobile Defense Platform)": HeroLossCondition.MOBILE_DEFENSE_PLATFORM,
    "Environment Card Killed Villain": HeroWinCondition.ENVIRONMENT,
    "Environment Target Killed Villain": HeroWinCondition.ENVIRONMENT,
    "HP Incapacitation (Heroes)": HeroLossCondition.VILLAINS_WIN,
    "Incapacitated Hero Ability": HeroWinCondition.INCAPACITATED,
    "Mars Base Explosion (Wagner)": HeroLossCondition.MARS_BASE_WAGNER,
    "Minion Overrun (Voss)": HeroLossCondition.GRAND_WARLORD_VOSS,
    "Omnitron's Devices After Omnitron died": HeroLossCondition.OMINTRON,
    "Relic Victory (Gloomweaver)": HeroWinCondition.GLOOMWEAVER,
    "Sentenced to Destruction (Celestial Tribunal)": HeroLossCondition.CELESTIAL_TRIBUNAl,
    "Terra Lunar Impulsion Beam (Baron Blade)": HeroLossCondition.BARON_BLADE,
    "The Crowd Turned Against the Heroes (Kaargra Warfang)": HeroLossCondition.KAARGRA_WARGANG,
    "The Environment was Destroyed (Deadline)": HeroLossCondition.DEADLINE,
    "Time Portal Closed (Silver Gulch 1883 )": HeroLossCondition.SILVER_GULCH,
    "Wager Master Alternate Loose Condition": HeroLossCondition.WAGER_MASTER,
    "Wager Master Alternate Loss Condition": HeroLossCondition.WAGER_MASTER,
    "Wager Master Alternate Win Condition": HeroWinCondition.WAGER_MASTER,
}

SELECTION_METHOD_GOOGLE_TO_RDS = {
    "": SelectionMethod.UNSPECIFIED,
    "Achievement Attempt": SelectionMethod.SPECIFIC_ATTEMPT,
    "Dice": SelectionMethod.RANDOM,
    "Player Choice": SelectionMethod.CHOICE,
    "Random Draw": SelectionMethod.RANDOM,
    "Randomizer Program": SelectionMethod.RANDOM,
    "Rematch": SelectionMethod.REMATCH,
    "Scenario": SelectionMethod.SPECIFIC_ATTEMPT,
    "SotM Video Game Random Button": SelectionMethod.RANDOM,
    "Thematic Team, Villain, Environment": SelectionMethod.SPECIFIC_ATTEMPT,
}

PLATFORM_GOOGLE_TO_RDS = {
    "": Platform.PHYSICAL,
    "Mobile Phone": Platform.MOBILE_UNKNOWN,
    "Other Video Game platform": Platform.OTHER,
    "Physical Cards": Platform.PHYSICAL,
    "Steam": Platform.STEAM,
    "Tablet (iPad or Android)": Platform.MOBILE_UNKNOWN,
}

GAME_LENGTH_GOOGLE_TO_RDS = {
    "": GameLength.UNRECORDED,
    "<30": GameLength.UNDER_THIRTY,
    "30-44": GameLength.UNDER_FORTY_FIVE,
    "45-59": GameLength.UNDER_ONE_HOUR,
    "60-90": GameLength.UNDER_TWO_HOURS,
    "90+": GameLength.MORE_THAN_TWO_HOURS,
}

# Remember to strip()
USERNAME_CONSOLIDATION = {
    "Aaro": "Aaron",
    "abnelson2@gmail.com": "abnelson2",
    "abnelsontwo": "abnelson2",
    "abnleson2": "abnelson2",
    "ALK": "ALK33389",
    "ALK333": "ALK33389",
    "ALkK": "ALK33389",
    "animus": "Animus",
    "Atariese": "Atariese Vinnessia",
    "atariese": "Atariese Vinnessia",
    "awd": "AWD",
    "Awd": "AWD",
    "awong": "Awong",
    "B.A Brownie": "B.A. Brownie",
    "baka": "BakaMatt",
    "Baka": "BakaMatt",
    "bolnerap": "Bolnerap",
    "camipco": "Camipco",
    "camipco@gmail.com": "Camipco",
    "Catdreaming": "CatDreaming",
    "cgrater": "CGrater",
    "Cgrater": "CGrater",
    "ChazIsdore": "ChazIsidore",
    "ChazIsidore ": "ChazIsidore",
    "CobaltChaos": "CobaltChaos56",
    "cozmic0": "Cozmic0",
    "Dandoio": "Dandolo",
    "deserter85": "Deserter85",
    "dolirn": "Dolirn",
    "dralanchiu": "Dralanchiu",
    "drb1004@yahoo.com": "drb1004",
    "drevilz4l": "Drevilz4l",
    "el Nate": "El Nate",
    "fig": "Fig",
    "FIG": "Fig",
    "fizzgig": "Fizzgig",
    "Fr SamB": "Fr. SamB",
    "Fry Guy": "FryGuy",
    "gaffa": "Gaffa",
    "Gafffa": "Gaffa",
    "G+": "Google Plus Game",
    "g+": "Google Plus Game",
    "Google": "Google Plus Game",
    "google +": "Google Plus Game",
    "Google game": "Google Plus Game",
    "GoogleGame": "Google Plus Game",
    "Google Game": "Google Plus Game",
    "gossamerica": "Gossamerica",
    "Hankriyd": "Hankroyd",
    "Hanroyd": "Hankroyd",
    "harkthrokgedunth@gmail": "harkthrokgedunt",
    "harkthrokgedunth@gmail.com": "harkthrokgedunt",
    "Humble Knight": "Humble-Knight",
    "Humble-knight": "Humble-Knight",
    "igarka": "Igarka",
    "igneus": "Igneus",
    "Jasomac": "JasoMac",
    "Jaybee": "JayBee",
    "jayBee": "JayBee",
    "jesnider": "Jesnider",
    "jmcgover": "Jmcgover",
    "Jpalmer197": "JPalmer1976",
    "Jpalmer1976": "JPalmer1976",
    "j1hopki1": "J1hopki1",
    "kamisage": "Kamisage",
    "kc9nxc": "Kc9nxc",
    "kilroy": "Kilroy",
    "lordofthefishes": "LordOfTheFishes",
    "Lordofthefishes": "LordOfTheFishes",
    "lynkfox": "Lynkfox",
    "markminnich": "mark minnich",
    "mikeb13603": "Mikeb13603",
    "mimito": "Mimito",
    "Mr.Fox": "Mr. Fox",
    "mrfettuccine": "MrFettuccine",
    "Mrfettuccine": "MrFettuccine",
    "Mspekkio": "MSpekkio",
    "much0gust0": "Much0Gust0",
    "nathanielbuck": "nathanielbuck14",
    "origamiswami": "origami swami",
    "origmiswami": "origami swami",
    "pelunar": "Pelunar",
    "Perlkonig": "Perlkönig",
    "potatogod93": "Potatogod93",
    "Powerhoubd_2000": "Powerhound_2000",
    "powerhound_2000": "Powerhound_2000",
    "rangertitch": "Rangertitch",
    "Rastlinie@gmail. Com": "Rastlinie",
    "reklyn": "Reklyn",
    "Robert Max freeman": "Robert Max Freeman",
    "robertmaxfreeman": "Robert Max Freeman",
    "robertmaxfrreeman": "Robert Max Freeman",
    "robertmfreeman": "Robert Max Freeman",
    "rookiebatman": "Rookiebatman",
    "rubric": "Rubric",
    "rwthompson23@gmail.com": "RWThompson23",
    "RWThompson23@gmail.com": "RWThompson23",
    "sickle5": "Sickle5",
    "Sheepfucker": "",
    "skalchemist": "Skalchemist",
    "skalchemist`": "Skalchemist",
    "skynight85": "Skynight85",
    "strahler": "Strahler",
    "TakeWalkerq": "TakeWalker",
    "TCPn": "TCP",
    "The_Gamemaniac/Kailen Clemont": "The_Gamemaniac",
    "The-Gamemaniac/Kailen Clemont": "The_Gamemaniac",
    "trickrune": "Trickrune",
    "UXM": "UXM266",
    "We're going to play, Steve": "Weregoingtoplaysteve",
    "x411811x": "X411811x",
    "XChylde": "XChylde17",
    "Xxvz": "XXVZ",
    "youlostme": "YouLostMe",
    "Test": "Test Game",
    "test": "Test Game",
}


pass
