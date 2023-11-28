word = input("Введите слово: ")
length = len(word)
if length % 2 == 0:
    middle_index = length // 2 - 1
    result = word[middle_index + 1]
else:
    middle_index = length // 2
    result = word[middle_index]
print("Результат:", result)