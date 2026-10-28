import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score = []
    lenght_args: int = len(sys.argv)
    if (lenght_args == 1):
        print(
            "No scores provided. Usage: python3"
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        for data in sys.argv[1:]:
            try:
                score.append(int(data))
            except ValueError:
                print(f"Invalid parameter: {data}")
        if (len(score) == 0):
            print(
                "No scores provided. Usage: python3"
                "ft_score_analytics.py <score1> <score2> ..."
            )
        else:
            total = sum(score)
            print("Scores processed: ", score)
            print("Total players: ", len(score))
            print("Total score: ", total)
            print("Average score: ", total / len(score))
            print("High Score: ", max(score))
            print("Low score: ", min(score))
            print("Score range: ", max(score) - min(score))


if __name__ == '__main__':
    main()
