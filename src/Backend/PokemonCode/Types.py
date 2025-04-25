from typing import Literal

PokemonType = Literal[
    "normal",
    "fire",
    "water",
    "grass",
    "electric",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dragon",
    "dark",
    "steel",
    "fairy",
]

PokemonNature = Literal[
    "NULL",
    "adamant",
    "bashful",
    "bold",
    "brave",
    "calm",
    "careful",
    "docile",
    "gentle",
    "hasty",
    "hardy",
    "impish",
    "jolly",
    "lax",
    "lonely",
    "mild",
    "modest",
    "naive",
    "naughty",
    "quiet",
    "quirky",
    "rash",
    "relaxed",
    "sassy",
    "serious",
    "timid",
]

PokemonAttackCategory = Literal["NULL", "physical", "special", "status"]
PokemonAttackObjetive = Literal["NULL", "single", "area", "itself", "partner"]

POKEMONSTATS = ["HP", "Atk", "Def", "SpA", "SpD", "Spe"]
HPTABLE = [
    "fighting",  # 0
    "flying",  # 1
    "poison",  # 2
    "ground",  # 3
    "rock",  # 4
    "bug",  # 5
    "ghost",  # 6
    "steel",  # 7
    "fire",  # 8
    "water",  # 9
    "grass",  # 10
    "electric",  # 11
    "psychic",  # 12
    "ice",  # 13
    "dragon",  # 14
    "dark",  # 15
]

NATURESTATSEFFECT = {
    "hardy": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "lonely": {'Atk': 1.1, 'Def': 0.9, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "brave": {'Atk': 1.1, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 0.9},
    "adamant": {'Atk': 1.1, 'Def': 1.0, 'Satk': 0.9, 'Sdef': 1.0, 'Spd': 1.0},
    "naughty": {'Atk': 1.1, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 0.9, 'Spd': 1.0},
    "bold": {'Atk': 0.9, 'Def': 1.1, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "docile": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "relaxed": {'Atk': 1.0, 'Def': 1.1, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 0.9},
    "impish": {'Atk': 1.0, 'Def': 1.1, 'Satk': 0.9, 'Sdef': 1.0, 'Spd': 1.0},
    "lax": {'Atk': 1.0, 'Def': 1.1, 'Satk': 1.0, 'Sdef': 0.9, 'Spd': 1.0},
    "timid": {'Atk': 0.9, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.1},
    "hasty": {'Atk': 1.0, 'Def': 0.9, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.1},
    "serious": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "jolly": {'Atk': 1.0, 'Def': 1.0, 'Satk': 0.9, 'Sdef': 1.0, 'Spd': 1.1},
    "naive": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 0.9, 'Spd': 1.1},
    "modest": {'Atk': 0.9, 'Def': 1.0, 'Satk': 1.1, 'Sdef': 1.0, 'Spd': 1.0},
    "mild": {'Atk': 1.0, 'Def': 0.9, 'Satk': 1.1, 'Sdef': 1.0, 'Spd': 1.0},
    "quiet": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.1, 'Sdef': 1.0, 'Spd': 0.9},
    "bashful": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
    "rash": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.1, 'Sdef': 0.9, 'Spd': 1.0},
    "calm": {'Atk': 0.9, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.1, 'Spd': 1.0},
    "gentle": {'Atk': 1.0, 'Def': 0.9, 'Satk': 1.0, 'Sdef': 1.1, 'Spd': 1.0},
    "sassy": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.1, 'Spd': 0.9},
    "careful": {'Atk': 1.0, 'Def': 1.0, 'Satk': 0.9, 'Sdef': 1.1, 'Spd': 1.0},
    "quirky": {'Atk': 1.0, 'Def': 1.0, 'Satk': 1.0, 'Sdef': 1.0, 'Spd': 1.0},
}
