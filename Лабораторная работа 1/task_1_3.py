list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Общее количество игроков
total_players = len(list_players)

# Разделение на две равные команды с использованием слайсирования
mid_point = total_players // 2
team1 = list_players[:mid_point]
team2 = list_players[mid_point:]

# Вывод результата
print(team1)
print(team2)
