from data_processor import DataProcessor, NumericProcessor
from data_processor import TextProcessor, LogProcessor
import typing


class DataStream:
    def __init__(self):
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        if proc in self.processors:
            print("Register already in list")
        else:
            self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            for pross in self.processors:
                if pross.validate(data):
                    pross.ingest(data)
                    break
            else:
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {data}"
                )

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        for process in self.processors:
            print(
                f"{process.__class__.__name__}: total {process.rank} "
                f"processed, ramaining {len(process.store)} on processor"
            )


def consume(proc: DataProcessor, times: int) -> None:
    if times > len(proc.store):
        print(
            "\n - ERROR ON CONSUME()-\n   "
            "Times can't be bigger than 'storage', "
            "should be times < len(store)\n"
        )
    else:
        for x in range(times):
            proc.output()


def main() -> None:
    datastream = DataStream()

    print("\nRegistering Numeric Processor...\n")

    print(
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is "
        "connected'}], 42, ['Hi', 'five']]"
    )
    np = NumericProcessor()
    datastream.register_processor(np)
    datastream.process_stream(
        [
            "Hello world",
            [3.14, -1, 2.71],
            [
                {
                    "log_level": "WARNING",
                    "log_message": "Telnet access! Use ssh instead",
                },
                {"log_level": "INFO", "log_message": "User wil is connected"},
            ],
            42,
            ["Hi", "five"],
        ]
    )
    datastream.print_processors_stats()

    print("\nRegistering Other DataProcessor...\n")
    print("Send the same batch again")
    tp = TextProcessor()
    lp = LogProcessor()
    datastream.register_processor(tp)
    datastream.register_processor(lp)
    datastream.process_stream(
        [
            "Hello world",
            [3.14, -1, 2.71],
            [
                {
                    "log_level": "WARNING",
                    "log_message": "Telnet access! Use ssh instead",
                },
                {"log_level": "INFO", "log_message": "User wil is connected"},
            ],
            42,
            ["Hi", "five"],
        ]
    )
    datastream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    consume(proc=np, times=3)
    consume(proc=tp, times=2)
    consume(proc=lp, times=1)
    datastream.print_processors_stats()


if __name__ == "__main__":
    main()
