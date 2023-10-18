import csv
import json
from collections import OrderedDict


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Чтение CSV файла и создание JSON файла
    with open(INPUT_FILENAME, "r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        # Список для хранения записей
        data = []

        for row in csv_reader:
            # Преобразование OrderedDict в обычный словарь
            row_dict = dict(row)

            # Добавление записи в список данных
            data.append(row_dict)

        # Запись данных в JSON файл с отступами равными 4
        with open(OUTPUT_FILENAME, "w") as json_file:
            json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
