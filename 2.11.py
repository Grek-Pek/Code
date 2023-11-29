year = int(input("Введите год: "))
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
if is_leap:
    print(year, "является високосным годом.")
else:
    print(year, "не является високосным годом.")
