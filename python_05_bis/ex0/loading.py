from importlib.metadata import distributions, version, PackageNotFoundError


def main() -> None:

    isMissing = False

    packages: list[str] = "numpy", "panda"

    for data in packages:
        try:
            version(data)
        except PackageNotFoundError:
            isMissing = True
            print(f"\n-- [Missing] {data} --")
            print(
                "\nTry: "
                "\nfor pip -> pip install -r requirements.txt"
                "\nfor poetry -> poetry install"
            )

    if isMissing is False:
        print("\nREAGENT STATUS: loading reagents...")
        print("\nChecking dependencies:")

        for content in distributions():
            print(
                f"[OK] {content.metadata['Name']} "
                f"({content.version}) - "
                f"{content.metadata.get('Summary')}"
            )
        print("\nPip vs Poetry:")
        print(
            "requirements.txt declares what to install;"
            "pip resolves it at install time."
            "\npyproject.toml declares the same constraints,"
            "and Poetry pins the resolved"
            "\nversions in poetry.lock so every install is identical."
        )
        print("\nAll reagents present and accounted for.")


if __name__ == '__main__':
    main()
