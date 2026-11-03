import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    player = ['Gabriel', 'Socrates', 'Spinoza', 'Sade', 'Senna']
    action = ['Run', 'Sleep', 'Eat', 'Drive', 'Play', 'Work']
    while True:
        name = random.choice(player)
        act = random.choice(action)
        tup: tuple
        tup = (name, act)
        yield tup


def consume_event(lst: list[tuple[str, str]]):
    i: int = 0
    while i < len(lst):
        data = random.choice(lst)
        print(f"Got event from list: {data}")
        lst.remove(data)
        yield lst


def main() -> None:
    i = 0
    lst: list[tuple[str, str]] = []
    info = gen_event()
    print("=== Game Data Stream Processor ===")
    for n in range(0, 1000):
        action: tuple[str, str] = next(info)
        print(f"Event {n}: Player {action[0]} did action {action[1]}")
    for i in range(0, 10):
        act: tuple[str, str] = next(info)
        lst.append(act)
    print(f"Built list of 10 events: {lst}")
    for x in consume_event(lst):
        print(f"Remains in list: {lst}")


if __name__ == "__main__":
    main()
