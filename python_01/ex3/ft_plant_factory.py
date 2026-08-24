class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.week_growth = 0

    def show(self) -> None:
        print(
            f"Created: {self.name}: {round(self.height, 2)}cm,"
            f"{self.age} days old"
        )

    def grow(self, evolution: float) -> None:
        self.height = self.height + evolution
        self.week_growth += evolution

    def old(self, stage: int) -> None:
        self.age = self.age + 1


def main() -> None:
    plants: list[list[str, float, int]] = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120],
    ]

    print("=== Plant Factory Output ===")
    for plant in plants:
        obj = Plant(plant[0], plant[1], plant[2])
        obj.show()


if __name__ == "__main__":
    main()
