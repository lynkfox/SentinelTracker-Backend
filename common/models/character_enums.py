from enum import Enum


class Character(Enum):
    @classmethod
    def has_member(cls, key) -> bool:
        """
        Quick check to see if key is within this class.
        """
        if isinstance(key, str):
            return key.lower() in cls.__members__
        elif isinstance(key, Enum):
            return key.name in cls.__members__
        else:
            return False


class Hero(Character):
    absolute_zero = "absolute_zero"
    akash_thriya = "akash_thriya"
    argent_adept = "the_argent_adept"
    bench_mark = "benchmark"
    bunker = "bunker"
    captain_cosmic = "captain_cosmic"
    chrono_ranger = "chrono_ranger"
    doctor_medico = "doctor_medico"
    expatriette = "expatriette"
    fanatic = "fanatic"
    guise = "guise"
    haka = "haka"
    harpy = "the_harpy"
    idealist = "idealist"
    knyfe = "k.n.y.f.e."
    la_comodora = "la_comodora"
    legacy = "legacy"
    lifeline = "lifeline"
    luminary = "luminary"
    mainstay = "mainstay"
    mr_fixer = "mr_fixer"
    naturalist = "the_naturalist"
    nightmist = "nightmist"
    ominitron_x = "omnitron_x"
    parse = "parse"
    ra = "ra"
    scholar = "the_scholar"
    setback = "setback"
    sky_scraper = "sky_scraper"
    southwest_sentinels = "the_southwest_sentinels"
    stuntman = "stuntman"
    tachyon = "tachyon"
    tempest = "tempest"
    unity = "unity"
    visionary = "the_visionary"
    wraith = "the_wraith"
    writhe = "writhe"


class Villain(Character):
    aeon_master = "aeon_master"
    akash_bhuta = "akash_bhuta"
    ambuscade = "ambuscade"
    apostate = "apostate"
    baron_blade = "baron_blade"
    biomancer = "biomancer"
    borr_the_unstable = "borr_the_unstable"
    bugbear = "bugbear"
    chairman = "the_chairman"
    chokepoint = "chokepoint"
    citizen_dawn = "citizen_dawn"
    citizens_hammer_and_anvil = "citizens_hammer_and_anvil"
    dark_mind = "dark_mind"
    deadline = "deadline"
    the_dreamer = "the_dreamer"
    empyreon = "empyreon"
    the_ennead = "the_ennead"
    ermine = "ermine"
    faultless = "faultless"
    friction = "friction"
    fright_train = "fright_train"
    glamour = "glamour"
    gloomweaver = "gloomweaver"
    grand_warlord_voss = "grand_warlord_voss"
    greazer_clutch = "greezer_clutch"
    infinitor = "infinitor"
    iron_legacy = "iron_legacy"
    kaargra = "kaargra_warfang"
    kismet = "kismet"
    la_capitan = "la_capitan"
    matriarch = "the_matriarch"
    miss_information = "miss_information"
    nixious_the_chosen = "nixious_the_chosen"
    oblivaeon = "oblivaeon"
    omnitron = "omnitron"
    the_operative = "the_operative"
    plague_rat = "plague_rat"
    progeny = "progeny"
    proletariat = "proletariat"
    ranek_kel_voss = "ranek_kel_voss"
    sanction = "sanction"
    sergeant_steel = "sergeant_steel"
    spite = "spite"
    voidsoul = "voidsoul"
    wager_master = "wager_master"


class Environment(Character):
    the_block = "the_block"
    celestial_tribunal = "celestial_tribunal"
    champion_studios = "champion_studios"
    court_of_blood = "court_of_blood"
    dok_thorath_capital = "dok_thorath_capital"
    enclave_of_the_endlings = "enclave_of_the_endlings"
    the_final_wasteland = "the_final_wasteland"
    fort_adamant = "fort_adamant"
    freedom_tower = "freedom_tower"
    insula_primalis = "insula_primalis"
    madame_mittermeiers = "madame_mittermeiers"
    maerynian_refuge = "maerynian_refuge"
    magmaria = "magmaria"
    megalopolis = "megalopolis"
    mobile_defense_platform = "mobile_defense_platform"
    mordengrad = "mordengrad"
    nexus_of_the_void = "nexus_of_the_void"
    omnitron_iv = "omnitron_iv"
    pike_industrial_complex = "pike_industrial_complex"
    realm_of_discord = "realm_of_discord"
    rook_city = "rook_city"
    ruins_of_atlantis = "ruins_of_atlantis"
    silver_gulch_1883 = "silver_gulch:_1883"
    temple_of_zhu_long = "the_temple_of_zhu_long"
    time_cataclysm = "time_cataclysm"
    tomb_of_anubis = "the_tomb_of_anubis"
    wagner_mars_base = "wagner_mars_base"


class AlternateTags(Character):
    freedom_five = "freedom_five"
    freedom_six = "freedom_six"
    termi_nation = "termi_nation"
    prime_wardens = "prime_wardens"
    xtreme_prime_wardens = "xtreme_prime_wardens"
    adamant = "adamant"
    dark_watch = "dark_watch"
    scion = "scion"
    team_villain = "team_villain"
    definitive = "definitive"  # definitive edition
    first_appearance = "first_appearance" # definitive edition

    spirit_of_the_void = "spirit_of_the_void"  # Akash hero
    dark_conductor = "dark_conductor"  # Argent
    supply_and_demand = "supply_and_demand"  # Benchmark
    gi = "gi"  # bunker
    requital = "requital"  # Captain Cosmic
    best_of_times = "best_of_times"  # Chrono Ranger
    malpractice = "malpractice"  # Dr Medico
    redeemer = "redeemer"  # Fanatic
    santa = "santa"  # Guise
    completionist = "complitionist"  # Guise
    eternal = "eternal"  # Haka
    super_sentai = "super_sentai"  # Idealist
    rogue_agent = "rogue_agent"  # KNYFE
    curse_of_the_black_spot = "curse_of_the_black_spot"  # La Coodora
    americas_greatest = "americas_greatest"  # Legacy
    americas_newest = "americas_newest"  # young legacy
    americas_cleverest = "americas_cleverest"  # Legacy
    bloodmage = "bloodmage"  # Lifeline
    heroic = "heroic"  # heroic luminary - and infinitor
    road_warrior = "road_warrior"  # Mainstay
    the_hunted = "the_hunted"  # Naturalist
    u = "u"  # omnitron-u
    fugue_state = "fugue_state"  # parse
    horus_of_the_two_horizon = "horus_of_the_two_horizon"  # Ra
    setting_sun = "setting_sun"  # Ra
    of_the_infinite = "of_the_infinite"  # Scholar
    extremist = "extremist" # Sky-scrapper
    action_hero = "action_hero"  # Stuntman
    super_scientific = "super_scientific"  # Tachyon
    dark = "dark"  # visionary
    unleashed = "unleashed"  # visionary
    rook_city = "rook_city"  # wraith
    cosmic_inventor = "cosmic_inventor"  # writhe

    mad_bomber = "mad_bomber"  # baron blade
    skinwalker = "skinwalker"  # gloomweaver
    trickster = "trickster"  # kismet
    cosmic = "cosmic"  # omnitron
    agent_of_gloom = "agent_of_gloom"  # spite
    definitive_mad_bomber = "definitive_mad_bomber"
    mecha = "mecha" # Akash Bhuta Definitive Edition
    mocktriarch = "mocktriarch" # Matriarch Definitive Edition
    definitive_cosmic = "definitive_cosmic" # Omnitron Definitive Edition
    censor = "censor" # Grand Warlord voss Definitive Edition
    sunrise = "sunrise" # Citizen Dawn Definitive Edition

ALTERNATE_TAG_DISPLAY_MAPPING = {
    AlternateTags.freedom_five: ", Freedom Five",
    AlternateTags.freedom_six: ", Freedom Six",
    AlternateTags.termi_nation: ", Termi-Nation",
    AlternateTags.prime_wardens: ", Prime Wardens",
    AlternateTags.xtreme_prime_wardens: ", XTREME Prime Wardens",
    AlternateTags.adamant: ", Adamant",
    AlternateTags.dark_watch: ", Dark Watch",
    AlternateTags.scion: ": Scion of OblivAeon",
    AlternateTags.team_villain: ": Team Villain",
    AlternateTags.definitive: ", Definitive",  # definitive edition
    AlternateTags.first_appearance: ", First Appearance of",
    AlternateTags.spirit_of_the_void: ": The Spirit Of The Void",  # Akash hero
    AlternateTags.dark_conductor: ": Dark Conductor",  # Argent
    AlternateTags.supply_and_demand: ": Supply And Demand",  # Benchmark
    AlternateTags.gi: ", GI",  # bunker
    AlternateTags.requital: ": Requital",  # Captain Cosmic
    AlternateTags.best_of_times: ", Best Of Times",  # Chrono Ranger
    AlternateTags.malpractice: ": Malpractice",  # Dr Medico
    AlternateTags.redeemer: ", Redeemer",  # Fanatic
    AlternateTags.santa: ", Santa",  # Guise
    AlternateTags.completionist: ", Completionist",  # Guise
    AlternateTags.eternal: ", Eternal",  # Haka
    AlternateTags.super_sentai: ", Super Sentai",  # Idealist
    AlternateTags.rogue_agent: ": Rogue Agent",  # KNYFE
    AlternateTags.curse_of_the_black_spot: "and The Curse Of The Black Spot",  # La Coodora
    AlternateTags.americas_greatest: ", Americas Greatest",  # Legacy
    AlternateTags.americas_newest: ", Americas Newest",  # young legacy
    AlternateTags.americas_cleverest: ", Americas Cleverest",  # Legacy
    AlternateTags.bloodmage: ": Bloodmage",  # Lifeline
    AlternateTags.heroic: ", Heroic",  # heroic luminary - and infinitor
    AlternateTags.road_warrior: ": Road Warrior",  # Mainstay
    AlternateTags.the_hunted: ", The Hunted",  # Naturalist
    AlternateTags.u: "- Omnitron-U",  # omnitron-u
    AlternateTags.fugue_state: ": Fugue State",  # parse
    AlternateTags.horus_of_the_two_horizon: ": Horus Of The Two Horizon",  # Ra
    AlternateTags.setting_sun: ": Setting Sun",  # Ra
    AlternateTags.of_the_infinite: " Of The_Infinite",  # Scholar
    AlternateTags.extremist: ", Extremist",  # Sky-Scraper
    AlternateTags.action_hero: ", Action Hero",  # Stuntman
    AlternateTags.super_scientific: ", Super Scientific",  # Tachyon
    AlternateTags.dark: ", Dark",  # visionary
    AlternateTags.unleashed: ": Unleashed",  # visionary
    AlternateTags.rook_city: ", Rook City",  # wraith
    AlternateTags.cosmic_inventor: ", Cosmic Inventor",  # writhe
    AlternateTags.mad_bomber: ", Mad Bomber",  # baron blade
    AlternateTags.skinwalker: ", Skinwalker",  # gloomweaver
    AlternateTags.trickster: ", Trickster",  # kismet
    AlternateTags.cosmic: ", Cosmic",  # omnitron
    AlternateTags.agent_of_gloom: ", Agent Of Gloom",  # spite
    AlternateTags.definitive_mad_bomber: ", Mad Bomber: Critcal Event!",
    AlternateTags.mecha: ": Critcal Event! Akash'Mecha", # Akash Bhuta Definitive Edition
    AlternateTags.mocktriarch: ": Critcal Event! MOCKtriarch", # Matriarch Definitive Edition
    AlternateTags.definitive_cosmic: ", Cosmic: Critcal Event! ", # Omnitron Definitive Edition
    AlternateTags.censor: ": Critcal Event! Censor", # Grand Warlord voss Definitive Edition
    AlternateTags.sunrise: ", Sunrise: Critcal Event! ", # Citizen Dawn Definitive Edition
}

HERO_DISPLAY_MAPPING = {
    Hero.akash_thriya: "Akash'Thriya",
    Hero.absolute_zero: "Absolute Zero",
    Hero.argent_adept: "The Argent Adept",
    Hero.bench_mark: "Benchmark",
    Hero.bunker: "Bunker",
    Hero.captain_cosmic: "Captain Cosmic",
    Hero.chrono_ranger: "Chrono Ranger",
    Hero.doctor_medico: "Doctor Medico",
    Hero.expatriette: "Expatriette",
    Hero.fanatic: "Fanatic",
    Hero.guise: "Guise",
    Hero.haka: "Haka",
    Hero.harpy: "The Harpy",
    Hero.idealist: "Idealist",
    Hero.knyfe: "K.N.Y.F.E.",
    Hero.la_comodora: "La Comodora",
    Hero.legacy: "Legacy",
    Hero.lifeline: "Lifeline",
    Hero.luminary: "Luminary",
    Hero.mainstay: "Mainstay",
    Hero.mr_fixer: "Mr. Fixer",
    Hero.naturalist: "The Naturalist",
    Hero.nightmist: "NightMist",
    Hero.ominitron_x: "Omnitron-X",
    Hero.parse: "Parse",
    Hero.ra: "Ra",
    Hero.scholar: "The Scholar",
    Hero.setback: "Setback",
    Hero.sky_scraper: "Sky-Scraper",
    Hero.southwest_sentinels: "The Southwest Sentinels",
    Hero.stuntman: "Stuntman",
    Hero.tachyon: "Tachyon",
    Hero.tempest: "Tempest",
    Hero.unity: "Unity",
    Hero.visionary: "The Visionary",
    Hero.wraith: "The Wraith",
    Hero.writhe: "Writhe",
}

VILLAIN_DISPLAY_MAPPING = {
    Villain.aeon_master: "Aeon Master",
    Villain.akash_bhuta: "Akash'Bhuta",
    Villain.ambuscade: "Ambuscade",
    Villain.apostate: "Apostate",
    Villain.baron_blade: "Baron Blade",
    Villain.biomancer: "Biomancer",
    Villain.borr_the_unstable: "Borr the Unstable",
    Villain.bugbear: "Bugbear",
    Villain.chairman: "The Chairman",
    Villain.chokepoint: "Chokepoint",
    Villain.citizen_dawn: "Citizen Dawn",
    Villain.citizens_hammer_and_anvil: "Citizens Hammer and Anvil",
    Villain.dark_mind: "Dark Mind",
    Villain.deadline: "Deadline",
    Villain.the_dreamer: "The Dreamer",
    Villain.empyreon: "Empyreon",
    Villain.the_ennead: "The Ennead",
    Villain.ermine: "Ermine",
    Villain.faultless: "Faultless",
    Villain.friction: "Friction",
    Villain.fright_train: "Fright Train",
    Villain.glamour: "Glamour",
    Villain.gloomweaver: "Gloomweaver",
    Villain.grand_warlord_voss: "Grand Warlord Voss",
    Villain.greazer_clutch: "Greezer Clutch",
    Villain.infinitor: "Infinitor",
    Villain.iron_legacy: "Iron Legacy",
    Villain.kaargra: "Kaargra Warfang",
    Villain.kismet: "Kismet",
    Villain.la_capitan: "La Capitan",
    Villain.matriarch: "The Matriarch",
    Villain.miss_information: "Miss Information",
    Villain.nixious_the_chosen: "Nixious The Chosen",
    Villain.oblivaeon: "OblivAeon",
    Villain.omnitron: "Omnitron",
    Villain.the_operative: "The Operative",
    Villain.plague_rat: "Plague Rat",
    Villain.progeny: "Progeny",
    Villain.proletariat: "Proletariat",
    Villain.ranek_kel_voss: "Ranek Kel'Voss",
    Villain.sanction: "Sanction",
    Villain.sergeant_steel: "Sergeant Steel",
    Villain.spite: "Spite",
    Villain.voidsoul: "Voidsoul",
    Villain.wager_master: "Wager Master",
}

ENVIRONMENT_DISPLAY_MAPPING= {
    Environment.the_block: "The Block",
    Environment.celestial_tribunal: "The Celestial Tribunal",
    Environment.champion_studios: "Champion Studios",
    Environment.court_of_blood: "The Court of Blood",
    Environment.dok_thorath_capital: "Dok'Thorath Capital",
    Environment.enclave_of_the_endlings: "Enclave of the Endlings",
    Environment.the_final_wasteland: "The Final Wasteland",
    Environment.fort_adamant: "Fort Adamant",
    Environment.freedom_tower: "Freedom Tower",
    Environment.insula_primalis: "Insula Primalis",
    Environment.madame_mittermeiers: "Madame Mittermeier's Fantastic Festival of Conundrums and Curiosities",
    Environment.maerynian_refuge: "Maerynian Refuge",
    Environment.magmaria: "Magmaria",
    Environment.megalopolis: "Megalopolis",
    Environment.mobile_defense_platform: "Mobile Defense Platform",
    Environment.mordengrad: "Mordengrad",
    Environment.nexus_of_the_void: "Nexus of the Void",
    Environment.omnitron_iv: "Omnitron-IV",
    Environment.pike_industrial_complex: "Pike Industrial Complex",
    Environment.realm_of_discord: "Realm of Discord",
    Environment.rook_city: "Rook City",
    Environment.ruins_of_atlantis: "Ruins of Atlantis",
    Environment.silver_gulch_1883: "Silver Gulch: 1883",
    Environment.temple_of_zhu_long: "The Temple of Zhu Long",
    Environment.time_cataclysm: "Time Cataclysm",
    Environment.tomb_of_anubis: "The Tomb of Anubis",
    Environment.wagner_mars_base: "Wagner Mars Base",
}
