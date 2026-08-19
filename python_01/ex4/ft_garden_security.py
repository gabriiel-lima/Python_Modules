class Plant:

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.__height = height
        self.__age = age
        self.week_growth = 0

    def show(self) -> None:
        print(f"Created: {self.name}: {self.__height:.1f}cm, {self.__age} days old")

    def grow(self, evolution: float) -> None:
        self.__height = self.__height + evolution
        self.week_growth += evolution
    
    def old(self, stage: int) -> None:
        self.__age = self.__age + 1
    
    def get_height(self) -> float:
        return(self.__height)
    
    def get_age(self) -> int:
        return(self.__age)
    
    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative\nHeight update rejected")
        else:
            self.__height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative\nAge update rejected")
        else:
            self.__age = value


def main() -> None:
    print("=== Garden Security System ===")
    obj = Plant("Rose", 175, 10)
    obj.show()
    obj.set_height(float(input("Height update: ")))
    obj.set_age(int(input("Age update: ")))
    obj.show()


if __name__ == "__main__":
    main()