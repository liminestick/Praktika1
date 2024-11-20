import numpy as np

# Функция для обработки строки
def process_line(line):
    # Разбиваем строку на элементы
    elements = line.split()
    # Преобразуем в список чисел, заменяя "N/A" на None
    numbers = [float(x) if x != 'N/A' else None for x in elements]

    # Заменяем "N/A" средним из соседних значений
    for i, num in enumerate(numbers):
        if num is None:
            left = numbers[i - 1] if i > 0 else None
            right = numbers[i + 1] if i < len(numbers) - 1 else None
            # Берем среднее от соседних, исключая None
            neighbors = [x for x in (left, right) if x is not None]
            numbers[i] = sum(neighbors) / len(neighbors) if neighbors else 0

    # Фильтруем только положительные четные значения
    filtered = [x for x in numbers if x > 0 and int(x) % 2 == 0]

    # Вычисляем среднее значение по оставшимся числам
    return np.mean(filtered) if filtered else 0


# Загрузка данных из файла
with open('third_task.txt', 'r') as file:
    lines = file.readlines()

# Обрабатываем каждую строку
results = [process_line(line) for line in lines]

with open('задание3/output.txt', 'w') as output_file:
    for avg in results:
        output_file.write("%.2f\n" % avg)

