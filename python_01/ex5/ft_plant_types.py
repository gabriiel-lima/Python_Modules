class Plant:

    def __init__(self, name: str, height: float, age: int, growth: float = 0):
        self.name = name
        self.__height = height
        self.__age = age
        self.growth = growth
        self.week_growth = 0

    def show(self) -> None:
        print(
            f"Created: {self.name}: {self.__height:.1f}cm,"
            f"{self.__age} days old"
        )

    def grow(self) -> None:
        self.__height = self.__height + self.growth
        self.week_growth += self.growth

    def old(self, stage: int) -> None:
        self.__age = self.__age + 1

    def get_height(self) -> float:
        return (self.__height)

    def get_age(self) -> int:
        return (self.__age)

    def set_height(self, value: float) -> None:
        if value < 0:
            print(
                f"{self.name}: Error, height can't be negative"
                f"\nHeight update rejected"
            )
        else:
            self.__height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(
                f"{self.name}: Error, age can't be negative"
                f"\nAge update rejected"
            )
        else:
            self.__age = value


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self.show()
        print(f"Color: {self.color}")
        print(f"{self.name} is blooming beatifully!")


class Tree(Plant):

    def __init__(
            self, name: str, height: float,
            age: int, trunk_diamenter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diamenter = trunk_diamenter

    def produce_shade(self) -> None:
        print("[Asking the oak to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of {self.get_height():.1f}"
            f"long and {self.trunk_diamenter:.1f}cm wide"
        )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        growth: float, harvest_season: str, older: int
    ) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season = harvest_season
        self.nutritional_value = 0
        self.older = older

    def show_vegetable(self) -> None:
        self.show()
        print(
            f"Harvest season: {self.harvest_season}"
            f"\nNutritional value {self.nutritional_value}"
        )

    def grow_vetetable(self) -> None:
        print("[make tomato grow and age for 20 days]")
        self.set_height(self.get_height() + self.growth)
        self.set_age(self.get_age() + self.older)
        self.nutritional_value = self.older


def main() -> None:
    print("=== Garden Plant Types ===")

    print("\n=== Flower")
    flower = Flower("Rose", 15, 10, "red")
    flower.show()
    flower.bloom()

    print("\n=== Tree")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable = Vegetable(
        name="Tomato",
        height=5, age=10, growth=42,
        harvest_season="abril", older=20
    )
    vegetable.show_vegetable()
    vegetable.grow_vetetable()
    vegetable.show_vegetable()


if __name__ == "__main__":
    main()
