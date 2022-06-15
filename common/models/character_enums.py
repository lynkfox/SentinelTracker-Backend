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

    def __bool__(self):
        return bool(self.value)

    def __str__(self):
        return str(self.value)


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
    knyfe = "knyfe"
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
    baccarat = "baccarat"
    doc_havoc = "doc_havoc"
    the_knight = "the_knight"
    lady_of_the_wood = "lady_of_the_wood"
    malichae = "malichae"
    necro = "necro"
    quicksilver = "quicksilver"
    starlight = "starlight"
    the_stranger = "the_stranger"
    tango_one = "tango_one"
    vanish = "vanish"
    drift = "drift"
    gargoyle = "gargoyle"
    gyrosaur = "gyrosaur"
    pyre = "pyre"
    terminus = "terminus"
    cricket = "cricket"
    cypher = "cypher"
    titan = "titan"
    echelon = "echelon"
    impact = "impact"
    magnificent_mara = "magnificent_mara"
    alpha = "alpha"


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
    kaargra_warfang = "kaargra_warfang"
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
    anathema = "anathema"
    dendron = "dendron"
    gray = "gray"
    the_ram = "the_ram"
    tiamat = "tiamat"
    dynamo = "dynamo"
    infernal_choir = "infernal_choir"
    mistress_of_fate = "mistress_of_fate"
    mythos = "mythos"
    outlander = "outlander"
    screamachine = "screamachine"
    oriphel = "oriphel"
    swarm_eater = "swarm_eater"
    vector = "vector"
    phase = "phase"
    celadroch = "celadroch"
    menagerie = "menagerie"
    the_organization = "the_organization"
    apex = "apex"
    fey_court = "fey_court"
    terraform = "terraform"


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

    blackwood_forest = "blackwood_forest"
    f_s_c_continuance_wanderer = "f_s_c_continuance_wanderer"
    halberd_experimental_research_center = "halberd_experimental_research_center"
    northspar = "northspar"
    st_simeons_catacombs = "st_simeons_catacombs"
    wandering_isle = "wandering_isle"
    catchwater_harbor_1929 = "catchwater_harbor_1929"
    chasm_of_a_thousand_nights = "chasm_of_a_thousand_nights"
    nightlore_citadel = "nightlore_citadel"
    vault_5 = "vault_5"
    windmill_city = "windmill_city"
    cybersphere = "cybersphere"
    superstorm_akela = "superstorm_akela"
    diamond_manor = "diamond_manor"


class AlternateTags(Character):
    # teams
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
    first_appearance = "first_appearance"  # definitive edition

    # heroes
    spirit_of_the_void = "spirit_of_the_void"  # Akash hero
    dark_conductor = "dark_conductor"  # Argent
    supply_and_demand = "supply_and_demand"  # Benchmark
    gi = "gi"  # bunker
    requital = "requital"  # Captain Cosmic
    best_of_times = "best_of_times"  # Chrono Ranger
    malpractice = "malpractice"  # Dr Medico
    redeemer = "redeemer"  # Fanatic
    santa = "santa"  # Guise
    completionist = "completionist"  # Guise
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
    extremist = "extremist"  # Sky-scrapper
    action_hero = "action_hero"  # Stuntman
    super_scientific = "super_scientific"  # Tachyon
    dark = "dark"  # visionary
    unleashed = "unleashed"  # visionary
    rook_city = "rook_city"  # wraith
    cosmic_inventor = "cosmic_inventor"  # writhe

    # villains
    mad_bomber = "mad_bomber"  # baron blade
    skinwalker = "skinwalker"  # gloomweaver
    trickster = "trickster"  # kismet
    cosmic = "cosmic"  # omnitron
    agent_of_gloom = "agent_of_gloom"  # spite
    definitive_mad_bomber = "definitive_mad_bomber"
    mecha = "mecha"  # Akash Bhuta Definitive Edition
    mocktriarch = "mocktriarch"  # Matriarch Definitive Edition
    definitive_cosmic = "definitive_cosmic"  # Omnitron Definitive Edition
    censor = "censor"  # Grand Warlord voss Definitive Edition
    sunrise = "sunrise"  # Citizen Dawn Definitive Edition

    # Cauldron teams
    first_response = "first_response"  # Cauldron team
    alt_1929 = "1929"  # NOTE TODO - Handle this in the api
    alt_2199 = "2199"  # NOTE TODO - Handle this in the api
    ministry_of_strategic_science = "ministry_of_strategic_science"  # Cauldron team
    renegade = "renegade"  # Cauldron team
    wasteland_ronin = "wasteland_ronin"  # Cauldron team

    # Cauldron heroes
    ace_of_swords = "ace_of_swords"  # Cauldron baccarat
    ace_of_sorrows = "ace_of_sorrows"  # Cauldron baccarat
    the_fair = "the_fair"  # Cauldron the knight
    the_berserker = "the_berserker"  # Cauldron the knight
    season_of_change = "season_of_change"  # Cauldron lady
    shardmaster = "shardmaster"  # Cauldron malichae
    warden_of_chaos = "warden_of_chaos"  # Cauldron necor
    the_uncanny = "the_uncanny"  # Cauldron quicksilver
    genesis = "genesis"  # Cauldron starlight
    nightlore_council = "nightlore_council"  # Cauldron starlight
    the_rune_carved = "the_rune_carved"  # Cauldron stranger
    ghost_ops = "ghost_ops"  # Cauldron tango one
    through_the_breach = "through_the_breach"  # Cauldron drift
    alt_1929_2199 = "1929/2199"  # Cauldron drift
    speed_demon = "speed_demon"  # Cauldron Gyrosaur
    the_unstable = "the_unstable"  # Cauldron Pyre
    swarming_protocol = "swarming_protocol"  # Cauldron Cypher

    # Cauldron villains
    evolved = "evolved"  # Cauldron Anathema
    hydra = "hydra"  # Cauldron tiamat
    windcolor = "windcolor"  # Cauldron dendron
    hivemind = "hivemind"  # Cauldron hivemind

    # rook city renegades heroes
    eclipse = "eclipse"  # expat
    fey_cursed = "fey_cursed"  # setback
    blackfist = "blackfist"
    mentor = "mentor"  # nightmist
    blood_raven = "blood_raven"  # harpy
    reporter = "reporter"  # alpha
    alt_2000 = "2000"  # alpha
    detective = "detective"  # wraith
    scavanger = "scavanger"  # unity
    stealth_suit = "stealth_suit"  # bunker
    haunted = "haunted"  # fanatic
    backdraft = "backdraft"  # ra
    werewolf = "werewolf"  # haka

    # rcr villains
    bear = "bear"  # Organization
    doctor_toxica = "doctor_toxica"  # Plague rat
    abomination = "abomination"  # spite
    soultaker = "soultaker"  # gloomweaver
    empowered = "empowered"  # kismet
    vainglorious = "vainglorious"  # ambuscade
    blood_leashed = "blood_leashed"  # apex
    war_girded = "war_girded"  # dagda & morrigan
    mark_iii = "mark_iii"  # terraform


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
    AlternateTags.spirit_of_the_void: ": The Spirit of the Void",  # Akash hero
    AlternateTags.dark_conductor: ": Dark Conductor",  # Argent
    AlternateTags.supply_and_demand: ": Supply And Demand",  # Benchmark
    AlternateTags.gi: ", GI",  # bunker
    AlternateTags.requital: ": Requital",  # Captain Cosmic
    AlternateTags.best_of_times: ", Best of Times",  # Chrono Ranger
    AlternateTags.malpractice: ": Malpractice",  # Dr Medico
    AlternateTags.redeemer: ", Redeemer",  # Fanatic
    AlternateTags.santa: ", Santa",  # Guise
    AlternateTags.completionist: ", Completionist",  # Guise
    AlternateTags.eternal: ", Eternal",  # Haka
    AlternateTags.super_sentai: ", Super Sentai",  # Idealist
    AlternateTags.rogue_agent: ": Rogue Agent",  # KNYFE
    AlternateTags.curse_of_the_black_spot: " and The Curse of the Black Spot",  # La Coodora
    AlternateTags.americas_greatest: ", America's Greatest",  # Legacy
    AlternateTags.americas_newest: ", America's Newest",  # young legacy
    AlternateTags.americas_cleverest: ", America's Cleverest",  # Legacy
    AlternateTags.bloodmage: ": Bloodmage",  # Lifeline
    AlternateTags.heroic: ", Heroic",  # heroic luminary - and infinitor
    AlternateTags.road_warrior: ": Road Warrior",  # Mainstay
    AlternateTags.the_hunted: ", The Hunted",  # Naturalist
    AlternateTags.u: " : Omnitron-U",  # omnitron-u
    AlternateTags.fugue_state: ": Fugue State",  # parse
    AlternateTags.horus_of_the_two_horizon: ": Horus of the Two Horizons",  # Ra
    AlternateTags.setting_sun: ": Setting Sun",  # Ra
    AlternateTags.of_the_infinite: " of the Infinite",  # Scholar
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
    AlternateTags.agent_of_gloom: ", Agent of Gloom",  # spite
    AlternateTags.definitive_mad_bomber: ", Mad Bomber: Critical Event!",
    AlternateTags.mecha: ": Critical Event! Akash'Mecha",  # Akash Bhuta Definitive Edition
    AlternateTags.mocktriarch: ": Critical Event! MOCKtriarch",  # Matriarch Definitive Edition
    AlternateTags.definitive_cosmic: ", Cosmic: Critical Event!",  # Omnitron Definitive Edition
    AlternateTags.censor: ": Critical Event! Censor",  # Grand Warlord voss Definitive Edition
    AlternateTags.sunrise: ", Sunrise: Critical Event!",  # Citizen Dawn Definitive Edition
    AlternateTags.first_response: ", First Response",  # Cauldron team
    AlternateTags.alt_1929: ": 1929",  # NOTE TODO - Handle this in the api
    AlternateTags.alt_2199: ": 2199",  # NOTE TODO - Handle this in the api
    AlternateTags.ministry_of_strategic_science: ": Ministry of Strategic Science",  # Cauldron team
    AlternateTags.renegade: ": Renegade",  # Cauldron team
    AlternateTags.wasteland_ronin: ": Wasteland Ronin",  # Cauldron team
    AlternateTags.ace_of_swords: ": Ace of Swords",  # Cauldron baccarat
    AlternateTags.ace_of_sorrows: ": Ace of Sorrows",  # Cauldron baccarat
    AlternateTags.the_fair: ", Fair",  # Cauldron the knight
    AlternateTags.the_berserker: ", Berserker",  # Cauldron the knight
    AlternateTags.season_of_change: ": Season of Change",  # Cauldron lady
    AlternateTags.shardmaster: ": Shardmaster",  # Cauldron malichae
    AlternateTags.warden_of_chaos: ": Warden of chaos",  # Cauldron necor
    AlternateTags.the_uncanny: ": The Uncanny",  # Cauldron quicksilver
    AlternateTags.genesis: ": Genesis",  # Cauldron starlight
    AlternateTags.nightlore_council: ": Nightlore Council",  # Cauldron starlight
    AlternateTags.the_rune_carved: ", The Rune Carved",  # Cauldron stranger
    AlternateTags.ghost_ops: ": Ghost Ops",  # Cauldron tango one
    AlternateTags.through_the_breach: ": Through the Breach",  # Cauldron drift
    AlternateTags.alt_1929_2199: ": 1929/2199",  # Cauldron drift
    AlternateTags.speed_demon: ", Speed demon",  # Cauldron Gyrosaur
    AlternateTags.the_unstable: ", The Unstable",  # Cauldron Pyre
    AlternateTags.evolved: ": Evolved",  # Cauldron Anathema
    AlternateTags.hydra: ", Hydra",  # Cauldron tiamat
    AlternateTags.windcolor: ", Windcolor",  # Cauldron dendron
    AlternateTags.hivemind: ", Hivemind",  # Cauldron Swarm Eater
    AlternateTags.swarming_protocol: ": Swarming Protocool",  # Cypher
    # rook city renegades heroes
    AlternateTags.eclipse: ": Eclipse",  # expat
    AlternateTags.fey_cursed: ", Fey-Cursed",  # setback
    AlternateTags.blackfist: ": Blackfist",  # mr fixer
    AlternateTags.mentor: ", Mentor",  # nightmist
    AlternateTags.blood_raven: ": Blood Raven",  # harpy
    AlternateTags.reporter: ", Reporter",  # alpha
    AlternateTags.alt_2000: ": 2000",  # alpha
    AlternateTags.detective: ", Detective",  # wraith
    AlternateTags.scavanger: ", Scavanger",  # unity
    AlternateTags.stealth_suit: ", Stealth Suit",  # bunker
    AlternateTags.haunted: ", Haunted",  # fanatic
    AlternateTags.backdraft: ", Backdraft",  # ra
    AlternateTags.werewolf: ", Berewolf",  # haka
    AlternateTags.bear: ": Critical Event! The Bear",  # Organization
    AlternateTags.doctor_toxica: ": Critical Event! Doctor Toxica",  # Plague rat
    AlternateTags.abomination: ", Abomination: Critical Event!",  # spite
    AlternateTags.soultaker: ", Soultaker: Critical Event!",  # gloomweaver
    AlternateTags.empowered: ", Empowered: : Critical Event!",  # kismet
    AlternateTags.vainglorious: ", Vainglorious: Critical Event! ",  # ambuscade
    AlternateTags.blood_leashed: ", Blood Leashed: Critical Event!",  # apex
    AlternateTags.war_girded: ", War Girded Dagada & Morrigan: Critical Event!",  # dagda & morrigan
    AlternateTags.mark_iii: ": Critical Event! Mark III",  # terraform
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
    Hero.baccarat: "Baccarat",
    Hero.doc_havoc: "Doc Havoc",
    Hero.the_knight: "The Knight",
    Hero.lady_of_the_wood: "Lady of the Wood",
    Hero.malichae: "Malichae",
    Hero.necro: "Necro",
    Hero.quicksilver: "Quicksilver",
    Hero.starlight: "Starlight",
    Hero.the_stranger: "The Stranger",
    Hero.tango_one: "Tango One",
    Hero.vanish: "Vanish",
    Hero.drift: "Drift",
    Hero.gargoyle: "Gargoyle",
    Hero.gyrosaur: "Gyrosaur",
    Hero.pyre: "Pyre",
    Hero.terminus: "Terminus",
    Hero.cricket: "Cricket",
    Hero.cypher: "Cypher",
    Hero.titan: "Titan",
    Hero.terminus: "Terminus",
    Hero.echelon: "Echelon",
    Hero.impact: "Impact",
    Hero.magnificent_mara: "Magnificent Mara",
    Hero.alpha: "Alpha",
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
    Villain.greazer_clutch: "Greazer Clutch",
    Villain.infinitor: "Infinitor",
    Villain.iron_legacy: "Iron Legacy",
    Villain.kaargra_warfang: "Kaargra Warfang",
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
    Villain.anathema: "Anathema",
    Villain.dendron: "Dendron",
    Villain.gray: "Gray",
    Villain.the_ram: "Ram, The",
    Villain.tiamat: "Tiamat",
    Villain.dynamo: "Dynamo",
    Villain.infernal_choir: "Infernal Choir, The",
    Villain.mistress_of_fate: "Mistress of Fate",
    Villain.mythos: "Mythos",
    Villain.outlander: "Outlander",
    Villain.screamachine: "Screamachine",
    Villain.oriphel: "Oriphel",
    Villain.swarm_eater: "Swarm Eater",
    Villain.vector: "Vector",
    Villain.phase: "Phase",
    Villain.celadroch: "Celadroch",
    Villain.menagerie: "Menagerie",
    Villain.apex: "Apex",
    Villain.fey_court: "The Fey Court",
    Villain.terraform: "Terraform",
    Villain.the_organization: "The Organization",
}

ENVIRONMENT_DISPLAY_MAPPING = {
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
    Environment.blackwood_forest: "Blackwood Forest",
    Environment.f_s_c_continuance_wanderer: "F.S.C Continuance Wanderer",
    Environment.halberd_experimental_research_center: "Halberd Experimental Research Center",
    Environment.northspar: "Northspar",
    Environment.st_simeons_catacombs: "St. Simeons Catacombs",
    Environment.wandering_isle: "Wandering Isle",
    Environment.catchwater_harbor_1929: "Catchwater Harbor: 1929",
    Environment.chasm_of_a_thousand_nights: "Chasm of a Thousand Nights",
    Environment.nightlore_citadel: "Nightlore Citadel",
    Environment.vault_5: "Vault 5",
    Environment.windmill_city: "Windmill City",
    Environment.cybersphere: "Cybersphere",
    Environment.superstorm_akela: "Superstorm Akela",
    Environment.diamond_manor: "Diamond Manor",
}
