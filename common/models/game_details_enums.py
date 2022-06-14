from dataclasses import dataclass, field
from typing import ClassVar


@dataclass(frozen=True)
class SelectionMethod:
    RANDOM: ClassVar[str] = (
        "Random",
    )  # any form of Randomizer - dice, app, eyes closed...
    CHOICE: ClassVar[str] = "Player Choice"  #
    REMATCH: ClassVar[
        str
    ] = "Rematch/Replay"  # Replaying or Rematch against the same villain
    EVENT: ClassVar[str] = "Event"  # Event/Collection card (Definitive)
    THEMATIC: ClassVar[
        str
    ] = "Themeatic"  # Game selection followed a theme: Team vs, all girls, all red hair ...
    SPECIFIC_ATTEMPT: ClassVar[
        str
    ] = "Specific Attempt"  # Attempting for a specific goal, so selected team specifically for that


@dataclass(frozen=True)
class HeroLossCondition:
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


@dataclass(frozen=True)
class HeroWinCondition:
    GLOOMWEAVER = "Destroy His Anchors (Gloomweaver Relics Destroyed)"
    ENVIRONMENT = "The House always Wins (Environment ends the Villain)"
    INCAPACITATED = "Down, but not Out! (Incapacitated Ability ends the Villain)"
    WAGER_MASTER = "Wager: Won! (Wager Master)"
