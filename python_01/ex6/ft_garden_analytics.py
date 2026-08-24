class Plant:

    def __init__(self, name: str, height: float, age: int, growth: float = 0):
        self._name: str = name
        self._height: float = height
        self._age: int = age
        self._growth: float = growth
        self._week_growth: float = 0
        self.statistic_grow = 0
        self.statistic_age = 0
        self.statistic_show = 0

    def show(self) -> None:
        print(f"{self._name}, {self._height:.1f}cm, {self._age} days old")
        self.statistic_show = self.statistic_show + 1

    def grow(self) -> int:
        self._height = self._height + self._growth
        self._week_growth += self._growth
        self.statistic_grow = self.statistic_grow + 1

    def age(self, age: int) -> None:
        self._age = self._age + age
        self.statistic_age = self.statistic_age + 1

    @staticmethod
    def check_age(value: int):
        if value > 365:
            print(f"Is {value} days more than a year -> True")
        else:
            print(f"Is {value} days more than a year -> False")

    @classmethod
    def anonymous(cls: 'Plant', height: float = 0, age: int = 0) -> 'Plant':
        return cls("Unknown plant", height, age)

    def statistics(self):
        print(f"[Statistics for {self._name}]")
        print(
            f"Stats: {self.statistic_grow} grow,"
            f"{self.statistic_age} age, {self.statistic_show} show"
        )


class Flower(Plant):

    def __init__(
        self, name: str, height: float, age: int,
        color: str, growth: float
    ) -> None:
        super().__init__(name, height, age, growth)
        self.color = color

    def bloom(self) -> None:
        self.show()
        print(f"Color: {self.color}")
        print(f"{self._name} has no bloomed yet")
        self.statistics()
        print(f"[asking the {self._name} grow to bloom]")
        self.grow()
        self.show()
        print(f"Color: {self.color}")
        print(f"{self._name} is blooming beatifully!")
        self.statistics()


class Seed(Flower):
    def __init__(
            self, name: str, height: float, age: int, color: str,
            seed: int, growth: float, old: int
    ) -> None:
        super().__init__(name, height, age, color, growth)
        self.seed = seed
        self.old: int = old

    def show_seed(self):
        self.show()
        print(f"Color: {self.color}")
        print(f"{self._name} has no bloomed yet")
        print("Seeds: 0")
        self.statistics()
        print(f"[asking the {self._name} grow to bloom]")
        self.grow()
        self.age(self.old)
        self.show()
        print(f"Color: {self.color}")
        print(f"{self._name} is blooming beatifully!")
        print(f"Seeds: {self.seed}")
        self.statistics()


class Tree(Plant):

    def __init__(
        self, name: str, height: float,
        age: int, trunk_diamenter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diamenter = trunk_diamenter
        self.shade = 0

    def show_tree(self) -> None:
        self.show()
        self.statistics()
        print(f"Shade: {self.shade}")

    def produce_shade(self) -> None:
        print("[Asking the oak to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of {self._height:.1f}"
            f"long and {self.trunk_diamenter:.1f}cm wide"
        )
        self.statistics()
        self.shade += 1
        print(f"Shade: {self.shade}")


def main() -> None:
    flower = Flower("Girassol", 15, 10, "yellow", 8)
    tree = Tree("Mangueira", 210, 400, 5)
    seed = Seed("Sunflower", 80, 45, "yellow", 42, 30, 20)

    print("== Garden Statistics ==")
    print("\n=== Check years old")
    Plant.check_age(30)
    Plant.check_age(400)

    print("\n== Flower")
    flower.bloom()

    print("\n== Tree")
    tree.show_tree()
    tree.produce_shade()

    print("\n== Seed")
    seed.show_seed()

    print("\n== Anonymous")
    anon = Plant.anonymous(0, 0)
    anon.show()
    anon.statistics()


if __name__ == "__main__":
    main()
