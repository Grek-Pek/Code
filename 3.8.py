shortest_word = None
while True:
    word = input("Введите слово: ")
    if word == "стоп":
        break
    if shortest_word is None or len(word) < len(shortest_word):
        shortest_word = word
if shortest_word:
    print("Самое короткое слово:", shortest_word)