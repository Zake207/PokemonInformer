from typing import Literal

PokemonType = Literal["NULL", 
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
                      "fairy"]

PokemonNature = Literal["NULL", "adamant", "bashful", "bold", "brave", "calm", "careful", 
    "docile", "gentle", "hasty", "hardy", "impish", "jolly", 
    "lax", "lonely", "mild", "modest", "naive", "naughty", 
    "quiet", "quirky", "rash", "relaxed", "sassy", "serious", 
    "timid"
]
NATURESTATSEFFECT = {
    "hardy":    (0, 0, 0, 0, 0, 0),
    "lonely":   (0, 0.1, -0.1, 0, 0, 0),
    "brave":    (0, 0.1, 0, 0, 0, -0.1),
    "adamant":  (0, 0.1, 0, -0.1, 0, 0),
    "naughty":  (0, 0.1, 0, 0, -0.1, 0),
    "bold":     (0, -0.1, 0.1, 0, 0, 0),
    "docile":   (0, 0, 0, 0, 0, 0),
    "relaxed":  (0, 0, 0.1, 0, 0, -0.1),
    "impish":   (0, 0, 0.1, -0.1, 0, 0),
    "lax":      (0, 0, 0.1, 0, -0.1, 0),
    "timid":    (0, -0.1, 0, 0, 0, 0.1),
    "hasty":    (0, 0, -0.1, 0, 0, 0.1),
    "serious":  (0, 0, 0, 0, 0, 0),
    "jolly":    (0, 0, 0, -0.1, 0, 0.1),
    "naive":    (0, 0, 0, 0, -0.1, 0.1),
    "modest":   (0, -0.1, 0, 0.1, 0, 0),
    "mild":     (0, 0, -0.1, 0.1, 0, 0),
    "quiet":    (0, 0, 0, 0.1, 0, -0.1),
    "bashful":  (0, 0, 0, 0, 0, 0),
    "rash":     (0, 0, 0, 0.1, -0.1, 0),
    "calm":     (0, -0.1, 0, 0, 0.1, 0),
    "gentle":   (0, 0, -0.1, 0, 0.1, 0),
    "sassy":    (0, 0, 0, 0, 0.1, -0.1),
    "careful":  (0, 0, 0, -0.1, 0.1, 0),
    "quirky":   (0, 0, 0, 0, 0, 0),
}


PokemonAttackCategory = Literal ["NULL", "physical", "special", "status"]

PokemonAttackObjetive = Literal ["NULL", "single", "area", "itself", "partner"]

HPTABLE = [
    "fighting",   # 0
    "flying",     # 1
    "poison",     # 2
    "ground",     # 3
    "rock",       # 4
    "bug",        # 5
    "ghost",      # 6
    "steel",      # 7
    "fire",       # 8
    "water",      # 9
    "grass",      # 10
    "electric",   # 11
    "psychic",    # 12
    "ice",        # 13
    "dragon",     # 14
    "dark"        # 15
]