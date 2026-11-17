import os
import sys


def main() -> None:
    if sys.prefix != sys.base_prefix or 'VIRTUAL_ENV' in os.environ:
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current python: {sys.executable}")
        name: str = os.environ['VIRTUAL_ENV'].split("/")
        print(f"Virtual Enviromment: {name[-1]}")
        print(f"Environment Path: {sys.prefix}")
        print(
            "\nSUCCESS: You are working in an isolated environment!"
            "\nSafe to install reagents without affecting"
            "\nthe global system"
        )
        print(f"Reagent installation path: {sys.path[-1]}")
    else:
        print(
            "\nLABORATORY STATUS: You are working in the open",
            "\n\nCurrent Python: /usr/bin/python3.11",
            "\nVirtual Environment: None detected",
            "\n\nWARNING: You are in the global environment!",
            "\nEvery reagent you install here leaks into the whole system.",
            "\n\nTo seal the laboratory, run:",
            "\npython3 -m venv lab_env",
            "\nsource lab_env/bin/activate # On Unix",
            "\nlab_env/Scripts/activate # On Windows",
            "\n\nThen run this program again."
        )


if __name__ == "__main__":
    main()
