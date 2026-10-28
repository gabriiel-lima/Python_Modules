import sys


def remove_duplicate(args: list) -> list:
    checked = set()
    new_list = []

    for data in args:
        if data[0] not in checked:
            new_list.append(data)
            checked.add(data[0])
        else:
            print(f"Redundant item '{data[0]}' - discarding")
    return (new_list)


def argument_processor(args: list) -> list:
    arguments: list[list[str | int]] = []

    for data in args[1:]:
        parts = str(data).split(":")

        if len(parts) == 2:
            try:
                quantity = int(parts[1])
            except ValueError as e:
                print(f"Quantity error for '{parts[1]}': {e}")
            else:
                arguments.append([parts[0], quantity])
        else:
            print(f"Error - invalid parameter '{parts[0]}'")

    clean_args = remove_duplicate(arguments)
    return (clean_args)


def main() -> None:
    print("\n=== Inventory System Analysis ===\n")
    args = argument_processor(sys.argv)
    if len(args) < 1:
        return
    storage = {}
    item_list = []
    quantity_items = []
    total_items: int
    for data in args:
        storage[data[0]] = data[1]
    print("\nGot inventory: ", storage)
    for key in storage:
        item_list.append(key)
    print("Item list: ", item_list)
    for value in storage.values():
        quantity_items.append(value)
    total_items = sum(quantity_items)
    print(
        f"\nTotal quantity of the {len(quantity_items)} "
        f"items: {total_items}\n"
    )
    maximo = 0
    least = 100
    for value in args:
        represent = ((value[1] / total_items) * 100)
        if represent > maximo:
            maximo = represent
            most_abundant = value
        if represent <= least:
            least = represent
            least_abundant = value
        print(
            f"Item {value[0]} represents "
            f"{round(represent, 1)}%"
        )
    print(
        f"\nItem most abundant: {most_abundant[0]} "
        f"with quantity: {most_abundant[1]}"
    )
    print(
        f"\nItem least abundant: {least_abundant[0]} "
        f"with quantity: {least_abundant[1]}"
    )
    storage.update({"magic_item": 1})
    print("\nUpdate inventory: ", storage)


if __name__ == "__main__":
    main()
