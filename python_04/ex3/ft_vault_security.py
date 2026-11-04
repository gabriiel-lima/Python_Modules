
def secure_archive(
    file_name: str, action: str, file_aux=None
) -> tuple[bool, str]:
    flag = True
    if action == "w":
        try:
            with open(file_aux, "r") as aux_file:
                content_aux = aux_file.read()
        except Exception as err:
            flag = False
            print(err)
        else:
            try:
                with open(file_name, "w") as main_file:
                    main_file.write(content_aux)
            except Exception as err:
                flag = False
                print(err)
        return flag, "Content successfully written to file"
    elif action == "r":
        try:
            with open(file_name, action) as new_file:
                content = new_file.read()
        except Exception as err:
            content = str(err)
            flag = False
    return flag, content


def main() -> None:
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("b.txt", "r"))

    print("Using 'secure_archive' to read from an inaccessible file: ")
    print(secure_archive("test.txt", "r"))

    print("Using 'secure_archive' to read from a regular file: ")
    print(secure_archive("a.txt", "r"))

    print("Using 'secure_archive' to write previous content to a new file: ")
    print(secure_archive("new.txt", "w", "a.txt"))


if __name__ == "__main__":
    main()
