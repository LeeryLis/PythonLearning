import json


def task() -> float:
    # Открываем и читаем JSON файл
    with open("input.json", "r") as file:
        data = json.load(file)

    # Переменная для суммы
    total = 0.0

    # Проходим по каждому словарю в списке
    for entry in data:
        # Получение значений "score" и "weight" из словаря
        score = entry["score"]
        weight = entry["weight"]
        # Вычисление произведения и добавление его к сумме
        total += score * weight

    return round(total, 3)

print(task())
