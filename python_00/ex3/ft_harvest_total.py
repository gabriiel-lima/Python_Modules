def ft_harvest_total():
    day = 0
    total = 0
    while day < 3:
        day += 1
        harvest = int(input(f"Day: {day} Harvest: ".format(day)))
        total += harvest
    print("Total harvest: ", total)


ft_harvest_total()
