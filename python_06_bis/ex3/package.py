from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.creature_type = creature_type

    @abstractmethod
    def attack(self) -> ...:
        pass

    def describe(self) -> ...:
        return f"{self.name} is a {self.creature_type} type {self.__class__.__name__}"


class TransformCapability(ABC):
    def __init__(self, istransform: bool):
        self.istransform = istransform

    @abstractmethod
    def transform() -> ...:
        pass

    @abstractmethod
    def revert() -> ...:
        pass


class Flameling(Creature):
    def __init__(self):
        super().__init__(name="Flameling", creature_type="Fire")

    def attack(self) -> str:
        return "Flameling uses Amber"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        TransformCapability.__init__(self, istransform=True)
        Creature.__init__(self, name="Shiftling", creature_type="Evolution")

    def attack(self) -> str:
        if self.istransform:
            return "Attacks normally."
        else:
            return "SUPER ATAQUE"

    def transform(self) -> None:
        self.istransform = False

    def revert(self) -> None:
        self.istransform = True


class Pyrodon(Creature):
    def __init__(self):
        super().__init__(name="Pyrodon", creature_type="Fire/Fly")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> Creature:
        pass

    @abstractmethod
    def create_envolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_envolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_envolved(self) -> Creature:
        pass


def main() -> None:
    flame = FlameFactory()
    evo = TransformCreatureFactory()
    print(flame.create_base().attack())
    print(flame.create_envolved().attack())
    t = evo.create_base()
    print(t.attack())
    t.transform()
    print(t.attack())
    t.revert()
    print(t.attack())


if __name__ == "__main__":
    main()
