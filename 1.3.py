def calculate_change(amount):
    banknotes = [1000, 100]
    coins = [10, 1]
    change = {}
    for note in banknotes:
        if amount >= note:
            num_notes = amount // note
            change[note] = num_notes
            amount %= note
    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            change[coin] = num_coins
            amount %= coin
    return change


amount = int(input("Введите сумму: "))
change = calculate_change(amount)
for money, count in change.items():
    print(f"{count} по {money} р")