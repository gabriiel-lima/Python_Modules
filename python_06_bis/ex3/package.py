from abc import ABC, abstractmethod



class Creature(ABC):
    @abstractmethod
    def attack() -> ...:
        pass

    def describe(self, name: str, desc: str) -> ...:
        return f"{name} is {desc}"


class Flameling(Creature):
    def __init__(self):
        pass

    def attack() -> str:
        return "Flameling uses Amber"


class Pyrodon(Creature):
    def attack() -> str:
        return "Pyrodon uses Flamethrower!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_envolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base() -> Flameling:
        return Flameling()
    

