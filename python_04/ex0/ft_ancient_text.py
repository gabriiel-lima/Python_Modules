import sys


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file>")
    else:
        print(f"Acessing file '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        else:
            content = file.read()
            print(f"---\n\n{content}\n\n---")
            print(f"File {sys.argv[1]} closed.")


if __name__ == "__main__":
    main()
