class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    a = Plant("Rose", 50, 18)
    b = Plant("Sunflower", 20, 20)
    c = Plant("Rose", 10, 8)
    print("== Garden Plant Registry")
    a.show()
    b.show()
    c.show()


if __name__ == "__main__":
    main()
