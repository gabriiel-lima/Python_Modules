def input_temperature(value: str) -> int:
    value_int: int = int(value)
    return (value_int)


def test_temperature(value: str) -> None:
    print(f"\nInput data is: '{value}'")
    try:
        input_temperature(value)
    except Exception:
        print(
            "Caught input_temperature error:"
            f"invalid literal for int() with base 10: '{value}'"
        )
    else:
        print(f"Temperature now is {value}°C")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature('25')
    test_temperature('abc')


if __name__ == '__main__':
    main()
