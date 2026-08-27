def input_temperature(value: int) -> int:
    if value < 0:
        raise ValueError(
            f"Caught input_temperature error: {value}°C"
            "is too cold for plants (min 0°C)"
        )
    elif value > 40:
        raise ValueError(
            f"Caught input_temperature error: {value}°C"
            "is too hot for plants (max 40°C)"
        )
    return (value)


def test_temperature(value: str) -> None:
    print(f"\nInput data is: '{value}'")
    try:
        value_int: int = int(value)
        input_temperature(value_int)
    except ValueError as e:
        print(e)
    else:
        print(f"Temperature now is {value}°C")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')
    test_temperature('55')
    print("\nAll tests completed - program didn't crash")


if __name__ == '__main__':
    main()
