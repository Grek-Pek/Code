letter = input("Введите букву: ")
count = int(input("Введите количество букв: "))
letters = input("Введите буквы через пробел: ").split()
max_count = 0
current_count = 0
for i in range(count):
    if letters[i] == letter:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0
print("Наибольшее количество повторений подряд буквы", letter, ":", max_count)
