def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != " area" and unit != "grams":
        print("Unknown unit type")

    print(f"{seed_type} seeds: {'cover' if unit == 'area' else ''} {quantity} {'square meters' if unit == 'area' else ''}{'packets available' if unit ==  'packets' else ''} {'grams total' if unit == 'grams' else ''}")
    