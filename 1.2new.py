import json
data = {
    "Фамилия": "Овер",
    "Имя": "Вульф",
    "Отчество": "Художников",
    "Телефон": "9834538958345",
    "Год рождения": "1939",
    "Город рождения": "Берлин",
    "Место учёбы": "Рейхстаг»",
}
with open("info.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

