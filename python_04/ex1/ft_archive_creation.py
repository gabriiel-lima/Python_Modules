import sys
import typing


def print_line(file: typing.TextIO) -> None:
    content = file.read()
    print(f"---\n\n{content}\n\n---")
    print(f"File {sys.argv[1]} closed.")
    print("\nTransform data:\n---\n")
    file = open(sys.argv[1], "r")
    line = file.readline()
    while line:
        print(f"{line.strip()}#")
        line = file.readline()
    print("\n---\n")


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
            print_line(file)
            file.close()
            new_file_name = str(input("Enter new file name (or empty): "))
            try:
                new_file = open(new_file_name, "w")
            except Exception:
                print("Not saving data.")
            else:
                print(f"Saving data to {new_file_name}")
                old_file = open(sys.argv[1], "r")
                old_line = old_file.read()
                content = [data + "#" for data in old_line.splitlines()]
                new_content = "\n".join(content)
                new_file.write(new_content)
                print(f"Data saving in file {new_file_name}.")
                old_file.close()
                new_file.close()


if __name__ == "__main__":
    main()
