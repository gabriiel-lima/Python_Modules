def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "area" and unit != "grams":
        print("Unknown unit type")
    else:
        print(
            f"{seed_type} seeds: {'cover' if unit == 'area' else ''} "
            f"{quantity} "
            f"{'square meters' if unit == 'area' else ''}"
            f"{'packets available' if unit == 'packets' else ''}"
            f"{'grams total' if unit == 'grams' else ''}"
        )
