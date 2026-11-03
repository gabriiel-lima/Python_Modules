import random


def main() -> None:
    initial_players: list[str] = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma',
        'Gregory', 'john', 'kevin', 'Liam'
    ]
    new_lst = [data.capitalize() for data in initial_players]
    only_cap = [data for data in initial_players if data.istitle()]
    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {initial_players}")
    print(f"New list with all names capitalize: {new_lst}")
    print(f"New list of capitalized names onlye: {only_cap}")
    score = [random.randrange(0, 1000) for x in range(len(initial_players))]
    print(score)
    score_dict = {key: value for (key, value) in zip(initial_players, score)}
    print(f"Score dict: {score_dict}")
    average = round(sum(score) / len(initial_players), 2)
    print(f"\nScore averege is: {average}")
    high = {k: v for (k, v) in zip(initial_players, score) if v > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
