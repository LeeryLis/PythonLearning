participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_first_group, participants_second_group, delimiter=","):
    # Формирование списков участников
    first_group = participants_first_group.split(delimiter)
    second_group = participants_second_group.split(delimiter)

    # Поиск общих участников (используя множества)
    common_participants = set(first_group) & set(second_group)

    # Преобразование множества общих участников обратно в список и его сортировка
    common_participants = sorted(list(common_participants))

    return common_participants

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter="|")

print("Общие участники:", common_participants)
