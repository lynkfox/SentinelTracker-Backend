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
from common.rds import create_rds_key


ENVIRONMENT_GOOGLE_TO_RDS_MAP = {
    "Celestial Tribunal": create_rds_key(
        Environment.celestial_tribunal, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Champion Studios": create_rds_key(
        Environment.champion_studios, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Dok'Thorath": create_rds_key(
        Environment.dok_thorath_capital, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Enclave of the Endlings": create_rds_key(
        Environment.enclave_of_the_endlings, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Fort Adamant": create_rds_key(
        Environment.fort_adamant, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Freedom Tower": create_rds_key(
        Environment.freedom_tower, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Insula Primalis": create_rds_key(
        Environment.insula_primalis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Madame Mittermeier's": create_rds_key(
        Environment.madame_mittermeiers, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Maerynian Refuge": create_rds_key(
        Environment.maerynian_refuge, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Magmaria": create_rds_key(Environment.magmaria, None, ENVIRONMENT_DISPLAY_MAPPING),
    "Megalopolis": create_rds_key(
        Environment.megalopolis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Mobile Defense Platform": create_rds_key(
        Environment.mobile_defense_platform, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Mordengrad": create_rds_key(
        Environment.mordengrad, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Nexus of the Void": create_rds_key(
        Environment.nexus_of_the_void, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Omnitron IV": create_rds_key(
        Environment.omnitron_iv, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Pike Industrial Complex": create_rds_key(
        Environment.pike_industrial_complex, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Realm of Discord": create_rds_key(
        Environment.realm_of_discord, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Rook City": create_rds_key(
        Environment.rook_city, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Ruins of Atlantis": create_rds_key(
        Environment.ruins_of_atlantis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Silver Gulch 1883": create_rds_key(
        Environment.silver_gulch_1883, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Temple of Zhu Long": create_rds_key(
        Environment.temple_of_zhu_long, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Block": create_rds_key(
        Environment.the_block, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Court of Blood": create_rds_key(
        Environment.court_of_blood, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "The Final Wasteland": create_rds_key(
        Environment.the_final_wasteland, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Time Cataclysm": create_rds_key(
        Environment.time_cataclysm, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Tomb of Anubis": create_rds_key(
        Environment.tomb_of_anubis, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
    "Wagner Mars Base": create_rds_key(
        Environment.wagner_mars_base, None, ENVIRONMENT_DISPLAY_MAPPING
    ),
}

VILLAIN_GOOGLE_TO_RDS_MAP = {
    "(None)": None,
    "Agent of Gloom Spite": create_rds_key(
        Villain.spite, AlternateTags.agent_of_gloom, VILLAIN_DISPLAY_MAPPING
    ),
    "Akash'bhuta": create_rds_key(Villain.akash_bhuta, None, VILLAIN_DISPLAY_MAPPING),
    "Ambuscade": create_rds_key(Villain.ambuscade, None, VILLAIN_DISPLAY_MAPPING),
    "Ambuscade (Vengeance)": create_rds_key(
        Villain.ambuscade, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Apostate": create_rds_key(Villain.apostate, None, VILLAIN_DISPLAY_MAPPING),
    "Baron Blade": create_rds_key(Villain.baron_blade, None, VILLAIN_DISPLAY_MAPPING),
    "Baron Blade (Vengeance)": create_rds_key(
        Villain.baron_blade, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Biomancer (Vengeance)": create_rds_key(
        Villain.biomancer, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Bugbear (Vengeance)": create_rds_key(
        Villain.bugbear, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Chokepoint": create_rds_key(Villain.chokepoint, None, VILLAIN_DISPLAY_MAPPING),
    "Citizen Dawn": create_rds_key(Villain.citizen_dawn, None, VILLAIN_DISPLAY_MAPPING),
    "Citizens Hammer and Anvil (Vengeance)": create_rds_key(
        Villain.citizens_hammer_and_anvil, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Cosmic Omnitron": create_rds_key(
        Villain.omnitron, AlternateTags.cosmic, VILLAIN_DISPLAY_MAPPING
    ),
    "Deadline": create_rds_key(Villain.deadline, None, VILLAIN_DISPLAY_MAPPING),
    "Ermine (Vengeance)": create_rds_key(Villain.ermine, None, VILLAIN_DISPLAY_MAPPING),
    "Friction (Vengeance)": create_rds_key(
        Villain.friction, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Fright Train (Vengeance)": create_rds_key(
        Villain.fright_train, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Gloomweaver": create_rds_key(Villain.gloomweaver, None, VILLAIN_DISPLAY_MAPPING),
    "Grand Warlord Voss": create_rds_key(
        Villain.grand_warlord_voss, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Greazer Clutch (Vengeance)": create_rds_key(
        Villain.greazer_clutch, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Infinitor": create_rds_key(Villain.infinitor, None, VILLAIN_DISPLAY_MAPPING),
    "Iron Legacy": create_rds_key(Villain.iron_legacy, None, VILLAIN_DISPLAY_MAPPING),
    "Kaargra Warfang": create_rds_key(
        Villain.kaargra_warfang, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Kismet": create_rds_key(Villain.kismet, None, VILLAIN_DISPLAY_MAPPING),
    "La Capitan": create_rds_key(Villain.la_capitan, None, VILLAIN_DISPLAY_MAPPING),
    "La Capitan (Vengeance)": create_rds_key(
        Villain.la_capitan, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Mad Bomber Blade": create_rds_key(
        Villain.baron_blade, AlternateTags.mad_bomber, VILLAIN_DISPLAY_MAPPING
    ),
    "Miss Information": create_rds_key(
        Villain.miss_information, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Miss Information (Vengeance)": create_rds_key(
        Villain.miss_information, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Omnitron": create_rds_key(Villain.omnitron, None, VILLAIN_DISPLAY_MAPPING),
    "Plague Rat": create_rds_key(Villain.plague_rat, None, VILLAIN_DISPLAY_MAPPING),
    "Plague Rat (Vengeance)": create_rds_key(
        Villain.plague_rat, AlternateTags.team_villain, VILLAIN_DISPLAY_MAPPING
    ),
    "Progeny": create_rds_key(Villain.progeny, None, VILLAIN_DISPLAY_MAPPING),
    "Proletariat (Vengeance)": create_rds_key(
        Villain.proletariat, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Sergeant Steel (Vengeance)": create_rds_key(
        Villain.sergeant_steel, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Skinwalker Gloomweaver": create_rds_key(
        Villain.gloomweaver, AlternateTags.skinwalker, VILLAIN_DISPLAY_MAPPING
    ),
    "Spite": create_rds_key(Villain.spite, None, VILLAIN_DISPLAY_MAPPING),
    "The Chairman": create_rds_key(Villain.chairman, None, VILLAIN_DISPLAY_MAPPING),
    "The Dreamer": create_rds_key(Villain.the_dreamer, None, VILLAIN_DISPLAY_MAPPING),
    "The Ennead": create_rds_key(Villain.the_ennead, None, VILLAIN_DISPLAY_MAPPING),
    "The Matriarch": create_rds_key(Villain.matriarch, None, VILLAIN_DISPLAY_MAPPING),
    "The Operative (Vengeance)": create_rds_key(
        Villain.the_operative, None, VILLAIN_DISPLAY_MAPPING
    ),
    "Tormented Infinitor": create_rds_key(
        Villain.infinitor, AlternateTags.heroic, VILLAIN_DISPLAY_MAPPING
    ),
    "Unstable Kismet": create_rds_key(
        Villain.kismet, AlternateTags.the_unstable, VILLAIN_DISPLAY_MAPPING
    ),
    "Vengeance Five": None,
    "Vengeance Style (Vengeance and Villains)": None,
    "Wager Master": create_rds_key(Villain.wager_master, None, VILLAIN_DISPLAY_MAPPING),
}

HERO_GOOGLE_TO_RDS_MAPPING = {
    "(None - Selecting this option here will remove your entry from the general statistics, but provide us with interesting stats for 2 hero games in a separate study)": None,
    "(none)": None,
    "(None)": None,
    "Absolute Zero": create_rds_key(Hero.absolute_zero, None, HERO_DISPLAY_MAPPING),
    "Absolute Zero: Freedom Five": create_rds_key(
        Hero.absolute_zero, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Absolute Zero: Freedom Six (Elemental Wrath)": create_rds_key(
        Hero.absolute_zero, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Absolute Zero: Termi-Nation": create_rds_key(
        Hero.absolute_zero, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Akash'Thriya": create_rds_key(Hero.akash_thriya, None, HERO_DISPLAY_MAPPING),
    "Akash'Thriya: Spirit of the Void": create_rds_key(
        Hero.akash_thriya, AlternateTags.spirit_of_the_void, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept": create_rds_key(Hero.argent_adept, None, HERO_DISPLAY_MAPPING),
    "Argent Adept: Dark Conductor (Kvothe)": create_rds_key(
        Hero.argent_adept, AlternateTags.dark_conductor, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept: Prime Warden": create_rds_key(
        Hero.argent_adept, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Argent Adept: XTREME Prime Warden": create_rds_key(
        Hero.argent_adept, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Benchmark": create_rds_key(Hero.bench_mark, None, HERO_DISPLAY_MAPPING),
    "Benchmark: Supply and Demand": create_rds_key(
        Hero.bench_mark, AlternateTags.supply_and_demand, HERO_DISPLAY_MAPPING
    ),
    "Bunker": create_rds_key(Hero.bunker, None, HERO_DISPLAY_MAPPING),
    "Bunker: Freedom Five": create_rds_key(
        Hero.bunker, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Bunker: Freedom Six (Engine of War)": create_rds_key(
        Hero.bunker, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Bunker: GI": create_rds_key(Hero.bunker, AlternateTags.gi, HERO_DISPLAY_MAPPING),
    "Bunker: Termi-Nation": create_rds_key(
        Hero.bunker, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic": create_rds_key(Hero.captain_cosmic, None, HERO_DISPLAY_MAPPING),
    "Captain Cosmic: Prime Warden": create_rds_key(
        Hero.captain_cosmic, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic: Requital": create_rds_key(
        Hero.captain_cosmic, AlternateTags.requital, HERO_DISPLAY_MAPPING
    ),
    "Captain Cosmic: XTREME Prime Warden": create_rds_key(
        Hero.captain_cosmic, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Chrono-Ranger": create_rds_key(Hero.chrono_ranger, None, HERO_DISPLAY_MAPPING),
    "Chrono-Ranger: Best of Times": create_rds_key(
        Hero.chrono_ranger, AlternateTags.best_of_times, HERO_DISPLAY_MAPPING
    ),
    "Dr. Medico: Void Guard": create_rds_key(
        Hero.doctor_medico, None, HERO_DISPLAY_MAPPING
    ),
    "Dr. Medico: Void Guard, Malpractice": create_rds_key(
        Hero.doctor_medico, AlternateTags.malpractice, HERO_DISPLAY_MAPPING
    ),
    "Expatriette": create_rds_key(Hero.expatriette, None, HERO_DISPLAY_MAPPING),
    "Expatriette: Dark Watch": create_rds_key(
        Hero.expatriette, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Fanatic": create_rds_key(Hero.fanatic, None, HERO_DISPLAY_MAPPING),
    "Fanatic: Prime Warden": create_rds_key(
        Hero.fanatic, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Fanatic: Redeemer": create_rds_key(
        Hero.fanatic, AlternateTags.redeemer, HERO_DISPLAY_MAPPING
    ),
    "Fanatic: XTREME Prime Warden": create_rds_key(
        Hero.fanatic, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Guise": create_rds_key(Hero.guise, None, HERO_DISPLAY_MAPPING),
    "Guise: Completionist": create_rds_key(
        Hero.guise, AlternateTags.completionist, HERO_DISPLAY_MAPPING
    ),
    "Guise: Santa": create_rds_key(
        Hero.guise, AlternateTags.santa, HERO_DISPLAY_MAPPING
    ),
    "Haka": create_rds_key(Hero.haka, None, HERO_DISPLAY_MAPPING),
    "Haka: Eternal": create_rds_key(
        Hero.haka, AlternateTags.eternal, HERO_DISPLAY_MAPPING
    ),
    "Haka: Prime Warden": create_rds_key(
        Hero.haka, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Haka: XTREME Prime Warden": create_rds_key(
        Hero.haka, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Harpy": create_rds_key(Hero.harpy, None, HERO_DISPLAY_MAPPING),
    "Harpy: Dark Watch": create_rds_key(
        Hero.harpy, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Idealist: Void Guard": create_rds_key(Hero.idealist, None, HERO_DISPLAY_MAPPING),
    "Idealist: Void Guard, Super Sentai": create_rds_key(
        Hero.idealist, AlternateTags.super_sentai, HERO_DISPLAY_MAPPING
    ),
    "K.N.Y.F.E.": create_rds_key(Hero.knyfe, None, HERO_DISPLAY_MAPPING),
    "K.N.Y.F.E.: Rogue Agent": create_rds_key(
        Hero.knyfe, AlternateTags.rogue_agent, HERO_DISPLAY_MAPPING
    ),
    "La Comodora": create_rds_key(Hero.la_comodora, None, HERO_DISPLAY_MAPPING),
    "La Comodora: Curse of the Black Spot": create_rds_key(
        Hero.la_comodora, AlternateTags.curse_of_the_black_spot, HERO_DISPLAY_MAPPING
    ),
    "Legacy": create_rds_key(Hero.legacy, None, HERO_DISPLAY_MAPPING),
    "Legacy: Freedom Five": create_rds_key(
        Hero.legacy, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Legacy: Greatest": create_rds_key(
        Hero.legacy, AlternateTags.americas_greatest, HERO_DISPLAY_MAPPING
    ),
    "Legacy: Young": create_rds_key(
        Hero.legacy, AlternateTags.americas_newest, HERO_DISPLAY_MAPPING
    ),
    "Lifeline": create_rds_key(Hero.lifeline, None, HERO_DISPLAY_MAPPING),
    "Lifeline: Blood Mage": create_rds_key(
        Hero.lifeline, AlternateTags.bloodmage, HERO_DISPLAY_MAPPING
    ),
    "Luminary": create_rds_key(Hero.luminary, None, HERO_DISPLAY_MAPPING),
    "Luminary: Heroic (Ivana)": create_rds_key(
        Hero.luminary, AlternateTags.heroic, HERO_DISPLAY_MAPPING
    ),
    "Mainstay: Void Guard": create_rds_key(Hero.mainstay, None, HERO_DISPLAY_MAPPING),
    "Mainstay: Void Guard, Road Warrior": create_rds_key(
        Hero.mainstay, AlternateTags.road_warrior, HERO_DISPLAY_MAPPING
    ),
    "Mr. Fixer": create_rds_key(Hero.mr_fixer, None, HERO_DISPLAY_MAPPING),
    "Mr. Fixer: Dark Watch": create_rds_key(
        Hero.mr_fixer, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Naturalist": create_rds_key(Hero.naturalist, None, HERO_DISPLAY_MAPPING),
    "Naturalist: Hunted": create_rds_key(
        Hero.naturalist, AlternateTags.the_hunted, HERO_DISPLAY_MAPPING
    ),
    "Nightmist": create_rds_key(Hero.nightmist, None, HERO_DISPLAY_MAPPING),
    "Nightmist: Dark Watch": create_rds_key(
        Hero.nightmist, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Omnitron-X": create_rds_key(Hero.ominitron_x, None, HERO_DISPLAY_MAPPING),
    "Omnitron-X: Omnitron-U": create_rds_key(
        Hero.ominitron_x, AlternateTags.u, HERO_DISPLAY_MAPPING
    ),
    "Parse": create_rds_key(Hero.parse, None, HERO_DISPLAY_MAPPING),
    "Parse: Fugue State": create_rds_key(
        Hero.parse, AlternateTags.fugue_state, HERO_DISPLAY_MAPPING
    ),
    "Ra": create_rds_key(Hero.ra, None, HERO_DISPLAY_MAPPING),
    "Ra: Horus of Two Horizons": create_rds_key(
        Hero.ra, AlternateTags.horus_of_the_two_horizon, HERO_DISPLAY_MAPPING
    ),
    "Ra: Setting Sun": create_rds_key(
        Hero.ra, AlternateTags.setting_sun, HERO_DISPLAY_MAPPING
    ),
    "Scholar": create_rds_key(Hero.scholar, None, HERO_DISPLAY_MAPPING),
    "Scholar: Of the Infinite": create_rds_key(
        Hero.scholar, AlternateTags.of_the_infinite, HERO_DISPLAY_MAPPING
    ),
    "Setback": create_rds_key(Hero.setback, None, HERO_DISPLAY_MAPPING),
    "Setback: Dark Watch": create_rds_key(
        Hero.setback, AlternateTags.dark_watch, HERO_DISPLAY_MAPPING
    ),
    "Sky-Scraper": create_rds_key(Hero.sky_scraper, None, HERO_DISPLAY_MAPPING),
    "Sky-Scraper: Extremist": create_rds_key(
        Hero.sky_scraper, AlternateTags.extremist, HERO_DISPLAY_MAPPING
    ),
    "Stuntman": create_rds_key(Hero.stuntman, None, HERO_DISPLAY_MAPPING),
    "Stuntman: Action Hero": create_rds_key(
        Hero.stuntman, AlternateTags.action_hero, HERO_DISPLAY_MAPPING
    ),
    "Tachyon": create_rds_key(Hero.tachyon, None, HERO_DISPLAY_MAPPING),
    "Tachyon: Freedom Five": create_rds_key(
        Hero.tachyon, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Tachyon: Freedom Six (Team Leader)": create_rds_key(
        Hero.tachyon, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Tachyon: Super Scientific": create_rds_key(
        Hero.tachyon, AlternateTags.super_scientific, HERO_DISPLAY_MAPPING
    ),
    "Tempest": create_rds_key(Hero.tempest, None, HERO_DISPLAY_MAPPING),
    "Tempest: Freedom Six (Sacrifice)": create_rds_key(
        Hero.tempest, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Tempest: Prime Warden": create_rds_key(
        Hero.tempest, AlternateTags.prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "Tempest: XTREME Prime Warden": create_rds_key(
        Hero.tempest, AlternateTags.xtreme_prime_wardens, HERO_DISPLAY_MAPPING
    ),
    "The Sentinels": create_rds_key(
        Hero.southwest_sentinels, None, HERO_DISPLAY_MAPPING
    ),
    "The Sentinels: Adamant": create_rds_key(
        Hero.southwest_sentinels, AlternateTags.adamant, HERO_DISPLAY_MAPPING
    ),
    "Unity": create_rds_key(Hero.unity, None, HERO_DISPLAY_MAPPING),
    "Unity: Freedom Six (Golem)": create_rds_key(
        Hero.unity, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Unity: Termi-Nation": create_rds_key(
        Hero.unity, AlternateTags.termi_nation, HERO_DISPLAY_MAPPING
    ),
    "Visionary": create_rds_key(Hero.visionary, None, HERO_DISPLAY_MAPPING),
    "Visionary: Dark": create_rds_key(
        Hero.visionary, AlternateTags.dark, HERO_DISPLAY_MAPPING
    ),
    "Visionary: Unleashed": create_rds_key(
        Hero.visionary, AlternateTags.unleashed, HERO_DISPLAY_MAPPING
    ),
    "Wraith": create_rds_key(Hero.wraith, None, HERO_DISPLAY_MAPPING),
    "Wraith: Freedom Five": create_rds_key(
        Hero.wraith, AlternateTags.freedom_five, HERO_DISPLAY_MAPPING
    ),
    "Wraith: Freedom Six (Price of Freedom)": create_rds_key(
        Hero.wraith, AlternateTags.freedom_six, HERO_DISPLAY_MAPPING
    ),
    "Wraith: Rook City": create_rds_key(
        Hero.wraith, AlternateTags.rook_city, HERO_DISPLAY_MAPPING
    ),
    "Writhe: Void Guard": create_rds_key(Hero.writhe, None, HERO_DISPLAY_MAPPING),
    "Writhe: Void Guard, Cosmic Inventor": create_rds_key(
        Hero.writhe, AlternateTags.cosmic_inventor, HERO_DISPLAY_MAPPING
    ),
}

WIN_CONDITION_GOOGLE_TO_RDS = {
    "": HeroWinCondition.STANDARD.value,
    "Ate Himself (Skinwalker Gloomweaver)": HeroLossCondition.SKINWALKER.value,
    "Did Not Protect Her (The Dreamer)": HeroLossCondition.DREAMER.value,
    "Engines Failed (Mobile Defense Platform)": HeroLossCondition.MOBILE_DEFENSE_PLATFORM.value,
    "Environment Card Killed Villain": HeroWinCondition.ENVIRONMENT.value,
    "Environment Target Killed Villain": HeroWinCondition.ENVIRONMENT.value,
    "HP Incapacitation (Heroes)": HeroLossCondition.VILLAINS_WIN.value,
    "Incapacitated Hero Ability": HeroWinCondition.INCAPACITATED.value,
    "Mars Base Explosion (Wagner)": HeroLossCondition.MARS_BASE_WAGNER.value,
    "Minion Overrun (Voss)": HeroLossCondition.GRAND_WARLORD_VOSS.value,
    "Omnitron's Devices After Omnitron died": HeroLossCondition.OMINTRON.value,
    "Relic Victory (Gloomweaver)": HeroWinCondition.GLOOMWEAVER.value,
    "Sentenced to Destruction (Celestial Tribunal)": HeroLossCondition.CELESTIAL_TRIBUNAl.value,
    "Sucker Punch, Final Dive, and other Destroy Cards": None,
    "Terra Lunar Impulsion Beam (Baron Blade)": HeroLossCondition.BARON_BLADE.value,
    "The Crowd Turned Against the Heroes (Kaargra Warfang)": HeroLossCondition.KAARGRA_WARGANG.value,
    "The Environment was Destroyed (Deadline)": HeroLossCondition.DEADLINE.value,
    "Time Portal Closed (Silver Gulch 1883 )": HeroLossCondition.SILVER_GULCH.value,
    "Wager Master Alternate Loose Condition": HeroLossCondition.WAGER_MASTER.value,
    "Wager Master Alternate Loss Condition": HeroLossCondition.WAGER_MASTER.value,
    "Wager Master Alternate Win Condition": HeroWinCondition.WAGER_MASTER.value,
}

SELECTION_METHOD_GOOGLE_TO_RDS = {
    "": SelectionMethod.UNSPECIFIED.value,
    "Achievement Attempt": SelectionMethod.SPECIFIC_ATTEMPT.value,
    "Dice": SelectionMethod.RANDOM.value,
    "Player Choice": SelectionMethod.CHOICE.value,
    "Random Draw": SelectionMethod.RANDOM.value,
    "Randomizer Program": SelectionMethod.RANDOM.value,
    "Rematch": SelectionMethod.REMATCH.value,
    "Scenario": SelectionMethod.SPECIFIC_ATTEMPT.value,
    "SotM Video Game Random Button": SelectionMethod.RANDOM.value,
    "Thematic Team, Villain, Environment": SelectionMethod.SPECIFIC_ATTEMPT.value,
}

PLATFORM_GOOGLE_TO_RDS = {
    "": Platform.PHYSICAL.value,
    "Mobile Phone": Platform.MOBILE_UNKNOWN.value,
    "Other Video Game platform": Platform.OTHER.value,
    "Physical Cards": Platform.PHYSICAL.value,
    "Steam": Platform.STEAM.value,
    "Tablet (iPad or Android)": Platform.MOBILE_UNKNOWN.value,
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
    "fizzgig": "Fizzgig",
    "Fr SamB": "Fr. SamB",
    "Fry Guy": "FryGuy",
    "gaffa": "Gaffa",
    "Gafffa": "Gaffa",
    "Google": "Google Plus Game",
    "google +": "Google Plus Game",
    "Google game": "Google Plus Game",
    "GoogleGame": "Google Plus Game",
    "gossamerica": "Gossamerica",
    "Hankriyd": "Hankroyd",
    "Hanroyd": "Hankroyd",
    "harkthrokgedunth@gmail": "harkthrokgedunt",
    "harkthrokgedunth@gmail.com": "harkthrokgedunt",
    "Humble Knight": "Humble-Knight",
    "Humble-knight": "Humble-Knight",
    "igarka": "Igarka",
    "igneus": "Igneus",
    "Jaybee": "JayBee",
    "jayBee": "JayBee",
    "jmcgover": "Jmcgover",
    "Jpalmer197": "JPalmer1976",
    "Jpalmer1976": "JPalmer1976",
    "kc9nxc": "Kc9nxc",
    "kilroy": "Kilroy",
    "lordofthefishes": "LordOfTheFishes",
    "Lordofthefishes": "LordOfTheFishes",
    "lynkfox": "Lynkfox",
    "markminnich": "mark minnich",
    "mikeb13603": "Mikeb13603",
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
}


pass
