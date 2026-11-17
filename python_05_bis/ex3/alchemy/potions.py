from ex2.elements import create_fire, create_water
from ex2.alchemy.elements import create_air, create_earth


def healing_potion() -> str:
    msg: str = "Healing potion brewed with"
    msg = msg + f" {create_air()} and {create_earth()}"
    return msg


def strength_potion() -> str:
    msg: str = "Healing potion brewed with"
    msg = msg + f" {create_fire()} and {create_water()}"
    return msg
