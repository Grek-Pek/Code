letter_num = int(input("Введите номер буквы английского алфавита (от 1 до 26): "))
letter = chr((letter_num - 1) % 26 + ord('A'))
result = letter
for i in range(1, 4):
    next_letter_num = (letter_num + i - 1) % 26 + 1
    next_letter = chr(next_letter_num + ord('A') - 1)
    result += next_letter
print("Результат:", result)
