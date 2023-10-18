numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Убираем пропуск (None) из списка и находим среднее арифметическое всех элементов
filtered_numbers = [num for num in numbers if num is not None]
average = sum(filtered_numbers) / len(numbers)

# Замена пропущенного элемента средним арифметическим
for i in range(len(numbers)):
    if numbers[i] is None:
        numbers[i] = average

print("Измененный список:", numbers)
