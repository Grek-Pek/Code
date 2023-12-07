def print_flight_dates(n, m):
    dates = []
    for day in range(n, 32, m):
        dates.append(str(day))
    print(" ".join(dates))


n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
print_flight_dates(n, m)
