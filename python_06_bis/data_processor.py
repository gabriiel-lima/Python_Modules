from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self):
        self.store: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        removed: tuple[int, str] = self.store.pop(0)
        return removed


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, int | float) for item in data)
        return isinstance(data, int | float)

    def ingest(self, data: any) -> None:
        if self.validate(data):
            if isinstance(data, int):
                self.store.append((self.rank, data))
                self.rank += 1
            else:
                for x in data:
                    self.store.append((self.rank, str(x)))
                    self.rank += 1
        else:
            print("Got exeption: Improper numeric data")


class TextProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for x in data:
                    self.store.append((self.rank, x))
                    self.rank += 1
            else:
                self.store.append((self.rank, data))
                self.rank += 1
        else:
            print("Got exeption: Improper text data")


class LogProcessor(DataProcessor):
    def __init__(self):
        super().__init__()

    def validate(self, data: any) -> bool:
        flag = True
        if isinstance(data, list) or isinstance(data, dict):
            if isinstance(data, dict):
                test = data.items()
                for x in test:
                    if not isinstance(x[0], str):
                        flag = False
                    elif not isinstance(x[1], str):
                        flag = False
        else:
            flag = False
        return flag
    
    def ingest(self, data: any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for d in data:
                    self.store.extend([[k, v] for k, v in d.items()])
            else:
                test = list(data.items())
                self.store.append((test[0][0], test[0][1]))
        else:
            print("INvalid dict")


def main() -> None:
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Processor ===")
    print("\nTesting Numeric Processor...")
    print("------------------------------")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    numeric.ingest('foo')
    print("Processing data: [1, 2, 3, 4, 5]")
    print("Extracting 3 values...")
    numeric.ingest([1, 2, 3])
    for i in range(3):
        outnum = numeric.output()
        print(f"Numeric Value {outnum[0]}: {outnum[1]}")
    print("\nTesting Text Processor...")
    print("-------------------------")
    print(f"Trying to validate input '42': {text.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'Word']")
    text.ingest(['Hello', 'Nexus', 'Word'])
    print("Extracting 1 value...")
    outtext = text.output()
    print(f"Numeric Value {outtext[0]}: {outtext[1]}")
    print("\nTesting Log Processor...")
    print("-------------------------")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")
    print(
        "Processing data:  '[{'log_level': 'NOTICE', 'log_message': "
        "'Connection to server'}, {'log_level': 'ERROR"
        "', 'log_message': 'Unauthorized access!!'}]'"
    )
    log.ingest([
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ])
    print("Extracting 2 values...")
    for x in range(2):
        logout = log.output()
        print(f"Log entry {x}: {logout[0]} : {logout[1]}")


if __name__ == "__main__":
    main()
