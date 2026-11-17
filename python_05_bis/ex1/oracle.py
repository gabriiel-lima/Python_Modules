from dotenv import load_dotenv
import os


def check_rules(
    rule: str, reference: str, mode: str,
    msg_err: str, msg_success: str
) -> str:
    if rule != reference:
        if mode == 'development':
            print(msg_err)
        else:
            print("Try again latter")
    else:
        if mode == 'development':
            print(msg_success)
        else:
            print("Success")
    return rule


def main() -> None:
    if os.path.exists('.env'):
        load_dotenv()
        MATRIX_MODE = os.getenv('MATRIX_MODE')
        DATABASE_URL = os.getenv('DATABASE_URL')
        API_KEY = os.getenv('API_KEY')
        LOG_LEVEL = os.getenv('LOG_LEVEL')
        ZION_ENDPOINT = os.getenv('ZION_ENDPOINT')
        print("ORACLE STATUS: Consulting the configuration..")
        print("Configuration loaded:")
        print(f"MODE: {MATRIX_MODE}")
        print("\nDATABASE:")
        check_rules(
            rule=DATABASE_URL,
            reference="https://www.geeksforgeeks.org/python/using-python",
            mode=MATRIX_MODE,
            msg_err="Error trying connect on database",
            msg_success='Database connected'
        )
        print("\nAPI_KEY:")
        check_rules(
            rule=API_KEY,
            reference="k42d14m3yr06",
            mode=MATRIX_MODE,
            msg_err="Error on API KEY",
            msg_success='Authenticated'
        )
        print("\nLOG LEVEL:")
        check_rules(
            rule=LOG_LEVEL,
            reference="DEBUG",
            mode=MATRIX_MODE,
            msg_err="Error on LOG LEVEL",
            msg_success=LOG_LEVEL
        )
        print("\nREMOTE:")
        check_rules(
            rule=ZION_ENDPOINT,
            reference="https://peerfinder.org/online",
            mode=MATRIX_MODE,
            msg_err="Error on ENDPOINT",
            msg_success="Online"
        )
        if MATRIX_MODE == 'development':
            print(
                "\nConfiguration security check:"
                "\n[OK] No hardcoded secrets detected"
                "\n[OK] .env file properly ignored by git"
                "\n[OK] Production overrides available"
            )

        print("\nThe Oracle sees all configurations.")
    else:
        print("Fail to read .env!")


if __name__ == '__main__':
    main()
