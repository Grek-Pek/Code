price1 = float(input("Введите цену первого товара: "))
price2 = float(input("Введите цену второго товара: "))
price3 = float(input("Введите цену третьего товара: "))
if price1 < price2 < price3:
    print("Акция!")
    total_amount = (price1 + price2 + price3) / 2
    print("К оплате:", total_amount)
elif price1 > price2 > price3:
    print("Акция!")
    total_amount = (price1 + price2 + price3) / 3
    print("К оплате:", total_amount)
else:
    print("К оплате:", price1 + price2 + price3)