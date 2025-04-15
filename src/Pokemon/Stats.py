from Types import HPTABLE, PokemonType
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class PokemonStats:
        _evs: Dict[str, int] = field(default_factory=lambda: 
            {"Hp": 0, "Atk": 0, "Def": 0, "Satk": 0, "Sdef": 0, "Spd": 0})
        _ivs: Dict[str, int] = field(default_factory=lambda: 
            {"Hp": 0, "Atk": 0, "Def": 0, "Satk": 0, "Sdef": 0, "Spd": 0})
        _base: Dict[str, int] = field(default_factory=lambda: 
            {"Hp": 0, "Atk": 0, "Def": 0, "Satk": 0, "Sdef": 0, "Spd": 0})
        _stats: Dict[str, int] = field(default_factory=lambda: 
            {"Hp": 0, "Atk": 0, "Def": 0, "Satk": 0, "Sdef": 0, "Spd": 0})
        _hptype = PokemonType
        
        @property
        def evs(self):
            return self._evs
        
        @property
        def ivs(self):
            return self._ivs
        
        @property
        def base(self):
            return self._base
        
        @property
        def stats(self):
            return self._stats
        
        @property
        def hptype(self):
            return self._hptype
        
        @property
        def _UpdateHpType(self):
            a = 0 if self.ivs['Hp'] % 2 == 0 else 1
            b = 0 if self.ivs['Atk'] % 2 == 0 else 1
            c = 0 if self.ivs['Def'] % 2 == 0 else 1
            d = 0 if self.ivs['Spd'] % 2 == 0 else 1
            e = 0 if self.ivs['Satk'] % 2 == 0 else 1
            f = 0 if self.ivs['Sdef'] % 2 == 0 else 1
            result = (a + 2*b + 4*c + 8*d + 16*e + 32*f) / 63
            self.hptype = HPTABLE[result]
            pass
        
        @property
        def _UpdateStats(self):
            # HP = floor(((2 * base + IV + floor(EV / 4)) * level) / 100) + level + 10
            self._sta

            self._stats = ()
            # Stat = floor((floor(((2 * base + IV + floor(EV / 4)) * level) / 100) + 5) * nature_modifier)

        
        @ivs.setter
        def ivs(self, new_ivs: List[int]):
            if len(new_ivs) != 6:
                raise ValueError("ERROR: You must introduce 6 integer numbers between 0 and 31.")
            for iv in new_ivs:
                if not iv in range(0,32):
                    raise ValueError("ERROR: iv's must be integer values between 0 and 31.")
            self.ivs = new_ivs
            self._UpdateHpType
            self._UpdateStats
            
        @evs.setter
        def evs(self, new_evs: List[int]):
            if len(new_evs) != 6:
                raise ValueError("ERROR: You must introduce 6 integer numbers between 0 and 255.")
            for ev in new_evs:
                if not ev in range(0,256):
                    raise ValueError("ERROR: iv's must be integer values between 0 and 255.")
            self._UpdateStats