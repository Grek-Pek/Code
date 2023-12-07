while True:
    num = int(input("Введите число: "))

    if num == 0:
        break

    if num % 3 == 0 and num % 7 == 0:
        print("Караул!")
        break
    elif num % 3 == 0:
        print("Несчастливое")
    elif num % 7 == 0:
        print("Опасное")
    else:
        print(num)