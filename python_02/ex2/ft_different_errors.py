def garden_operations(operation_number):
    if operation_number == 0:
        try:
            int("abc")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
    elif operation_number == 1:
        try:
            10 / 0
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisorError: {e}")
    elif operation_number == 2:
        try:
            with open("non_existent_file.txt", "r") as file:
                file.read()
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
    elif operation_number == 3:
        try:
            "abc" + 42
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    elif operation_number == 4:
        print("Operation completed successfully")


def test_error_types():
    print("== Garden Error Types Demo")
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except FileNotFoundError as e:
            print(e)
        except TypeError as e:
            print(e)
    print("\nAll error types tested successfully!")


def main():
    test_error_types()


if __name__ == '__main__':
    main()
