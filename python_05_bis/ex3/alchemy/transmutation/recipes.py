from ex2.alchemy.elements import create_air
from ..potions import strength_potion
from ex2.elements import create_fire


def lead_to_gold() -> str:
    msg: str = "Recipe transmuting Lead to Gold: "
    msg = msg + f"Gold: brew '{create_air()}' and "
    msg = msg + f"'{strength_potion()}' mixed with '{create_fire()}'"
    return msg
