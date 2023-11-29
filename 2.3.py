city1 = input("Введите название города для июля: ")
city2 = input("Введите название города для августа: ")
if (city1 == "Тула" and city2 == "Пенза") or (city1 == "Пенза" and city2 == "Тула") and city1 != city2:
    print("ДА")
else:
    print("НЕТ")