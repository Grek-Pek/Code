category = input("Введите категорию товара: ")
if category.lower() == "продукты":
    price = float(input("Введите цену: "))
    if price < 100:
        print("Попробуйте нашу выпечку! ")
    elif 100 <= price <= 500:
        print("Как насчёт орехов в шоколаде? ")
    elif price > 500:
        print("Попробуйте экзотические фрукты! ")
else:
    print("Загляните в товары для дома! ")
