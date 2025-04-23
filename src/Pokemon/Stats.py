"""
Main module that defines the logic for calculating Pokémon statistics.

Includes handling of base stats, IVs, EVs, nature, and the Hidden Power type.
"""

from Types import HPTABLE, PokemonType, NATURESTATSEFFECT, PokemonNature
from dataclasses import dataclass, field
from typing import Dict
from math import floor


@dataclass
class PokemonStats:
    """
    Class that represents a Pokémon's stats and provides methods
    to calculate its final stats and Hidden Power type.

    Attributes:
        _evs (Dict[str, int]): Effort Values (EVs) for each stat.
        _ivs (Dict[str, int]): Individual Values (IVs) for each stat.
        _base (Dict[str, int]): Base stats of the Pokémon.
        _stats (Dict[str, int]): Calculated stats based on base, IVs, EVs, and nature.
        _nature (PokemonNature): Nature of the Pokémon that affects stat calculation.
        _hptype (PokemonType): Type of the calculated Hidden Power move.
    """

    _evs: Dict[str, int] = field(
        default_factory=lambda: {key: 0 for key in ["Hp", "Atk", "Def", "Satk", "Sdef", "Spd"]}
    )
    _ivs: Dict[str, int] = field(
        default_factory=lambda: {key: 0 for key in ["Hp", "Atk", "Def", "Satk", "Sdef", "Spd"]}
    )
    _base: Dict[str, int] = field(
        default_factory=lambda: {key: 0 for key in ["Hp", "Atk", "Def", "Satk", "Sdef", "Spd"]}
    )
    _stats: Dict[str, int] = field(
        default_factory=lambda: {key: 0 for key in ["Hp", "Atk", "Def", "Satk", "Sdef", "Spd"]}
    )
    _nature: PokemonNature = "hardy"
    _hptype: PokemonType = "fighting"

    @property
    def evs(self) -> Dict[str, int]:
        """Get the current Effort Values (EVs) of the Pokémon."""
        return self._evs

    @evs.setter
    def evs(self, new_evs: Dict[str, int]):
        required_keys = {"Hp", "Atk", "Def", "Satk", "Sdef", "Spd"}
        if set(new_evs.keys()) != required_keys:
            raise ValueError(f"EVs must contain exactly these keys: {required_keys}")
        if not all(0 <= value <= 255 for value in new_evs.values()):
            raise ValueError("Each EV must be between 0 and 255.")
        self._evs = new_evs
        self._UpdateStats()

    @property
    def ivs(self) -> Dict[str, int]:
        """Get the Individual Values (IVs) of the Pokémon."""
        return self._ivs

    @ivs.setter
    def ivs(self, new_ivs: Dict[str, int]):
        required_keys = {"Hp", "Atk", "Def", "Satk", "Sdef", "Spd"}
        if set(new_ivs.keys()) != required_keys:
            raise ValueError(f"IVs must contain exactly these keys: {required_keys}")
        if not all(0 <= value <= 31 for value in new_ivs.values()):
            raise ValueError("Each IV must be between 0 and 31.")
        self._ivs = new_ivs
        self._UpdateHpType()
        self._UpdateStats()

    @property
    def base(self) -> Dict[str, int]:
        """Get the base stats of the Pokémon."""
        return self._base

    @property
    def stats(self) -> Dict[str, int]:
        """Get the calculated stats of the Pokémon."""
        return self._stats

    @property
    def hptype(self) -> PokemonType:
        """Get the current Hidden Power type of the Pokémon."""
        return self._hptype

    @property
    def nature(self) -> PokemonNature:
        """Get the nature of the Pokémon."""
        return self._nature

    @nature.setter
    def nature(self, new_nature: PokemonNature):
        self._nature = new_nature
        self._UpdateStats()

    def _UpdateHpType(self):
        """
        Recalculates the Pokémon's Hidden Power type based on its IVs.
        """
        bits = [
            int(self.ivs[stat] % 2 == 1) for stat in ["Hp", "Atk", "Def", "Spd", "Satk", "Sdef"]
        ]
        index = sum(bit << i for i, bit in enumerate(bits))
        result = floor((index * 15) / 63)
        self._hptype = HPTABLE[result]

    def _UpdateStats(self):
        """
        Recalculates the Pokémon's final stats using base stats, IVs, EVs, and nature.
        """
        self._stats['Hp'] = (
            floor(((2 * self.base['Hp'] + self.ivs['Hp'] + floor(self.evs['Hp'] / 4)) * 50) / 100)
            + 50
            + 10
        )

        for stat in ['Atk', 'Def', 'Satk', 'Sdef', 'Spd']:
            nature_modifier = NATURESTATSEFFECT[self.nature][stat]
            base_calc = (
                floor(
                    ((2 * self.base[stat] + self.ivs[stat] + floor(self.evs[stat] / 4)) * 50) / 100
                )
                + 5
            )
            self._stats[stat] = floor(base_calc * nature_modifier)
