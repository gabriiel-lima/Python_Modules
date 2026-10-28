import sys


def main() -> None:
    print("=== Command Quest ===")
    print("Program name: ", sys.argv[0])
    if (len(sys.argv) > 1):
        print("Arguments received: ", len(sys.argv) - 1)
        for pos, args in enumerate(sys.argv):
            if (pos > 0):
                print(f"Argument {pos}: {args}")
    else:
        print("No arguments provided!")
    print("Total arguments:", len(sys.argv))


if __name__ == '__main__':
    main()
