from data_processor import DataProcessor, NumericProcessor
from data_processor import TextProcessor, LogProcessor
import typing


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]):
        pass


class Json:
    def __init__(self):
        self.store: list[tuple[int, str]] = []

    def make_save(self, data: tuple[int, str]):
        self.store.append((f"item_{data[0]}", data[1]))

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        js = dict(self.store)
        print(f"{js}")


class Csv:
    def __init__(self):
        self.store: list[tuple[int, str]] = []
    
    def make_save(self, data: tuple[int, str]):
        self.store.append((data[1]))
    
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        for peer in self.store:
            print(f"{peer},", end=" ")
        print('\n')


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
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data\n")
        else:
            for process in self.processors:
                print(
                    f"{process.__class__.__name__}: total {process.rank} "
                    f"processed, ramaining {len(process.store)} on processor"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            plugin.store.clear()
            try:
                for count in range(nb):
                    plugin.make_save(proc.output())
            except IndexError:
                break
            plugin.process_output(proc.store)


def main() -> None:
    js = Json()
    csv = Csv()
    datastream = DataStream()
    print("\n=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...\n")
    datastream.print_processors_stats()
    print("Registering Processors\n")
    print(
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is "
        "connected'}], 42, ['Hi', 'five']]\n"
    )
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
   
    datastream.register_processor(np)
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
    print("\nSend 3 processed data from each processor to a CSV plugin: ")
    datastream.output_pipeline(2, csv)
    datastream.print_processors_stats()
    print(
        "\nSend another batch of data: "
        "[21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], "
        "[{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE', "
        "'log_message': 'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], 'World hello']"
    )

    datastream.process_stream(
        [
            21,
            [
                "I love AI",
                "LLMs are wonderful",
                "Stay healthy",
            ],
            [
                {
                    "log_level": "ERROR",
                    "log_message": "500 server crash",
                },
                {
                    "log_level": "NOTICE",
                    "log_message": "Certificate expires in 10 days",
                },
            ],
            [32, 42, 64, 84, 128, 168],
            "World hello",
        ]
    )
    datastream.print_processors_stats()
    print("\nSend 5 processed data from each processor to a JSON plugin:")
    datastream.output_pipeline(5, js)

if __name__ == '__main__':
    main()
