while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 + num2 , num1 // num2
        print("Результат сложения:", result)
        break
    except ValueError:
        print("Ошибка: введены некорректные данные. Пожалуйста, введите только целочисленные значения.")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
print("Выход из программы")