class GardenError(Exception):
    def __init__(self, mensage: str = "Unknow GardenError"):
        self.mensage = mensage
        super().__init__(mensage)


class WaterError(GardenError):
    def __init__(self, mensage: str = "Unknow WaterError"):
        self.mensage = mensage
        super().__init__(mensage)


class PlantError(GardenError):
    def __init__(self, mensage: str = "Unknow PlantError"):
        self.mensage = mensage
        super().__init__(mensage)


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


def test_plant() -> None:
    raise PlantError('The tomato is wilting!')


def main() -> None:
    print("=== Custom Garden Error Demo ===\n")

    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")

    print("Testing GardenErrors...")
    errors = [test_plant, test_water]
    for error in errors:
        try:
            error()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly")


if __name__ == '__main__':
    main()
