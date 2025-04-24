"""
Main module that defines the pokemon's metadata's logic
"""

from Types import PokemonType
from dataclasses import dataclass, field
from typing import Tuple


@dataclass
class Metadata:
    _name: str = "Missingno"
    _id: int = -1
    _weight: int = -1
    _height: int = -1
    _ability: str = "NULL"
    _types: Tuple[PokemonType, PokemonType] = field(default_factory=lambda: ["normal", "normal"])
    _object: str = "NULL"

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    @property
    def ability(self):
        return self._ability

    @property
    def types(self):
        return self._types

    @property
    def object(self):
        return self._object
