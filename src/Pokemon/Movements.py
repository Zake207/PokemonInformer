from Types import PokemonType, PokemonAttackCategory, PokemonAttackObjetive
from dataclasses import dataclass

@dataclass
class Movement:
        _name: str = "NULL"
        _category: PokemonAttackCategory = "NULL"
        _damage: int = -1
        _pp: int = -1
        _type: PokemonType = "NULL"
        _precision: int = -1
        _objetive: PokemonAttackObjetive = "NULL"
        _effect: str = "NULL"
        _priority: int = -1
        _contact: bool = False
        
        @property
        def name(self):
            return self._name

        @property
        def category(self):
            return self._category

        @property
        def damage(self):
            return self._damage

        @property
        def pp(self):
            return self._pp

        @property
        def type(self):
            return self._type

        @property
        def precision(self):
            return self._precision

        @property
        def objetive(self):
            return self._objetive

        @property
        def effect(self):
            return self._effect

        @property
        def priority(self):
            return self._priority

        @property
        def contact(self):
            return self._contact
        
@dataclass
class Moveset:
        pass