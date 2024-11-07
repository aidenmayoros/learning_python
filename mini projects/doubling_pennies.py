def penny_rich():
    print(
        "Calculating if you got a penny a day and doubled it how much you would have in a month"
    )
    total = 0
    for x in range(1, 31):
        total *= 2
        total += 0.01
        print(f"on day {x} the total is {round(total, 2)}")


penny_rich()
