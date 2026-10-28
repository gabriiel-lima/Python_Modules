import math


def first_pos() -> tuple:
    pos = []
    print("Get a first set of coordinates")
    while (True):
        position = input(
            "Enter new coordinates as floats in"
            "format 'x,y,z': ").replace(" ", "").split(',')
        for data in position:
            try:
                pos.append(float(data))
            except ValueError:
                pos.clear()
        if (len(pos) == 3):
            break
        else:
            print("Invalid syntax")
            pos.clear()
            continue
    cordenate = tuple(pos)
    return (cordenate)


def second_pos() -> tuple:
    pos = []
    print("Get a second set of coordinates")
    while (True):
        position = input(
            "Enter new coordinates as floats in"
            "format 'x,y,z': ").replace(" ", "").split(',')
        for data in position:
            try:
                pos.append(float(data))
            except ValueError as e:
                pos.clear()
                print(f"Error on parameter {data}: {e}")
        if (len(pos) == 3):
            break
        else:
            pos.clear()
            print("Invalid syntax")
            continue
    cordenate = tuple(pos)
    return (cordenate)


def main() -> None:
    print("=== Game Coordinate Sysrem ===\n")
    position = first_pos()
    print("Got a first tuple: ", position[:3])
    print(f"It includes: X={position[0]}, Y={position[1]}, Z={position[2]}")
    value = math.sqrt(
        (position[0]-0)**2 + (position[1]-0)**2 + (position[2]-0)**2
    )
    print("Distance:", round(value, 4))
    print("")
    sec_position = second_pos()
    print(sec_position)
    distance = math.sqrt(
        (position[0]-sec_position[0])**2 +
        (position[1]-sec_position[1])**2 +
        (position[2]-sec_position[2])**2
    )
    print(
        "Distance beetween the 2 sets of coordinates: ", round(distance, 4)
    )


if (__name__ == "__main__"):
    main()
