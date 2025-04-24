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

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: PokemonAttackCategory):
        self._category = category

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, dmg: int):
        self._damage = dmg

    @property
    def pp(self):
        return self._pp

    @pp.setter
    def pp(self, pp: int):
        self._pp = pp

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: PokemonType):
        self._type = type

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, precision: int):
        self._precision = precision

    @property
    def objetive(self):
        return self._objetive

    @objetive.setter
    def objetive(self, objetive: PokemonAttackObjetive):
        self._objetive = objetive

    @property
    def effect(self):
        return self._effect

    @effect.setter
    def effect(self, effect: str):
        self._effect = effect

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority: int):
        self._priority = priority

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, contact: bool):
        self._contact = contact
