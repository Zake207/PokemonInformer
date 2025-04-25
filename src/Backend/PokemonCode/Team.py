from Pokemons import PokemonDB
from typing import List
from dataclasses import dataclass, field


@dataclass
class PokemonTeam:
    _members: List[PokemonDB] = field(default_factory=lambda: [PokemonDB() for _ in range(6)])
    _anotations: str = "-"
    _format: str = "-"

    @property
    def members(self) -> set[PokemonDB]:
        return self._members

    @property
    def anotations(self) -> str:
        return self._anotations

    @property
    def format(self) -> str:
        return self._format
