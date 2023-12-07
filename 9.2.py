while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: Введите целочисленное значение!")

result = num1 + num2
print("Сумма двух чисел =", result)