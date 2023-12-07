try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 + num2
    print("Результат:", result)
except ValueError:
    print("Ошибка: Введены некорректные данные. Введите целочисленные значения.")