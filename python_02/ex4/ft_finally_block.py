class PlantError(Exception):
    def __init__(self, mensage: str = "Unknow PlantError"):
        self.mensage = mensage
        super().__init__(mensage)


def water_plant(plant_name: str) -> None:
    if plant_name[0].isupper():
        print(f"{plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering() -> None:
    print("Testing valid plants...")
    print("Opening watering system")
    plants = ["Tomato", "Watermelon", "Pineple"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Close watering system")
    print("\nTesting invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "watermelon", "Pineple"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Close watering system")


def main() -> None:
    print("=== Garden Watering System ==\n")
    test_watering()
    print("\nCleanup always happens, even with errors")


if __name__ == "__main__":
    main()
