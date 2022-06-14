from enum import Enum


class SQLEnum(Enum):
    def __bool__(self):
        return bool(self.value)


class Platform(SQLEnum):
    PHYSICAL = "Physical"
    TABLE_TOP_SIMULATOR = "Table Top Simulator"
    STEAM = "Steam"
    APPLE = "Apple"
    ANDROID = "Android"
    OTHER = "Other"
    MOBILE_UNKNOWN = "Mobile (Unknown Brand)"
    PLAYTESTING = "Playtesting"


class GameLength(SQLEnum):
    UNRECORDED = "Not Known / Not Recorded"
    UNDER_THIRTY = "Less than 30 mins"
    UNDER_FORTY_FIVE = "Less than 45 mins"
    UNDER_ONE_HOUR = "Less than 1 hour"
    UNDER_TWO_HOURS = "Less than 2 hours"
    MORE_THAN_TWO_HOURS = "More than 2 hours"


class BoxSet(SQLEnum):
    FIRST_EDITION = "First Edition"
    ENHANCED_EDITION = "Enhanced Edition"
    DEFINITIVE_EDITION = "Definitive Edition"
    ROOK_CITY = "Rook City"
    INFERNAL_RELICS = "Infernal Relics"
    SHATTERED_TIMELINES = "Shattered Timelines"
    VENGEANCE = "Vengeance"
    WRATH_OF_THE_COSMOS = "Wrath of the Cosmos"
    VILLAINS = "Villains of the Multiverse"
    OBLIVAEON = "OblivAeon"
    UNITY = "Mini: Unity"
    SCHOLAR = "Mini: Scholar"
    GUISE = "Mini: Guise"
    STUNTMAN = "Mini: Stuntman"
    BENCHMARK = "Mini: Benchmark"
    VOID_GUARD = "Mini: The Void Guard"
    AMBUSCADE = "Mini: Ambuscade"
    MISS_INFORMATION = "Mini: Miss Information"
    WAGER_MASTER = "Mini: Wager Master"
    CHOKEPOINT = "Mini: Chokepoint"
    FINAL_WASTELAND = "Mini: The Final Wasteland"
    SILVER_GULCH = "Mini: Silver Gulch 1883"
    OMNITRON_IV = "Mini: Omnitron-IV"
    CELESTIAL_TRIBUNAL = "Mini: The Celestial Tribunal"
    CAULDRON = "Cauldron"
    CAULDRON_EXPERIMENTAL = "Cauldron: Experimental"
    CAULDRON_STORMFALL = "Cauldron: Stormfall"
    CAULDRON_ADRIFT = "Cauldron: Adrift"
    ROOK_CITY_RENEGADES = "Rook City: Renegades"


class SelectionMethod(SQLEnum):
    UNSPECIFIED = "Unspecified"
    RANDOM = "Random"
    # any form of Randomizer - dice, app, eyes closed...
    CHOICE = "Player Choice"
    REMATCH = "Rematch/Replay"
    # Replaying or Rematch against the same villain
    EVENT = "Event"
    # Event/Collection card (Definitive)
    THEMATIC = "Thematic"
    # Game selection followed a theme: Team vs, all girls, all red hair ...
    SPECIFIC_ATTEMPT = "Specific Attempt"
    # Attempting for a specific goal, so selected team specifically for that


class GameMode(SQLEnum):
    NORMAL = "Normal"
    VILLAINS = "Team Villains"
    OBLIVAEON = "OblivAeon"
    DEFINITIVE = "Definitive"
    MIXED = "Mixed"
    # Definitive and normal characters mixed


class HeroLossCondition(SQLEnum):
    VILLAINS_WIN = "Heroes Defeated by the Villains"
    SKINWALKER = "Consumed! (Gloomweaver, Skinwalker)"
    DREAMER = "Fell to her Dreams (The Dreamer)"
    GRAND_WARLORD_VOSS = "Earth, Overrun! (Grand Warlord Voss)"
    OMINTRON = "Lives on through it's devices (Omnitron)"
    MOBILE_DEFENSE_PLATFORM = "Engines Failed! (Mobile Defense Platform)"
    MARS_BASE_WAGNER = "3, 2, 1, ZERO! (Mars Wagner Base)"
    CELESTIAL_TRIBUNAl = "Found: Guilty! (Celestial Tribunal)"
    BARON_BLADE = "Terra-Lunar Impulsion Beam, Activate! (Baron Blade)"
    DEADLINE = "For your own Good! (Deadline)"
    SILVER_GULCH = "Lost in Time! (Silver Gulch 1883)"
    WAGER_MASTER = "Wager: Lost! (Wager Master)"
    KAARGRA_WARGANG = "Lost the Crowds Favor (Kaargra Warfang)"
    OBILVAEON = "Only the Void Left (OblivAeon)"


class HeroWinCondition(SQLEnum):
    STANDARD = "The Hero's Triumph (Villain(s) Incapacitated)"
    GLOOMWEAVER = "Destroy His Anchors (Gloomweaver Relics Destroyed)"
    ENVIRONMENT = "The House always Wins (Environment ends the Villain)"
    INCAPACITATED = "Down, but not Out! (Incapacitated Ability ends the Villain)"
    WAGER_MASTER = "Wager: Won! (Wager Master)"
