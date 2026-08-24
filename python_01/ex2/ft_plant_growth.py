class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.week_growth = 0

    def show(self):
        print(f"{self.name}: {round(self.height, 2)}cm, {self.age} days old")

    def grow(self, evolution: float):
        self.height = self.height + evolution
        self.week_growth += evolution

    def old(self, stage: int):
        self.age = self.age + 1


def main():
    plant1 = Plant("Rose", 25, 30)
    i = 1

    print("== Garden Plan Growth ==")
    plant1.show()
    while i <= 7:
        print(f"== Day {i} ==")
        plant1.grow(0.8)
        plant1.old(1)
        plant1.show()
        i += 1
    print(f"Growth this week: {plant1.week_growth}")


if __name__ == "__main__":
    main()
