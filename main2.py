import os
import math

# Создаем папку "задание2", если её нет
os.makedirs('задание2', exist_ok=True)

# Загрузка данных из файла
with open('second_task.txt', 'r') as file:
    lines = file.readlines()

# Операция для каждой строки: взятие квадратного корня от каждого положительного числа и целая часть от суммы
column_results = []
for line in lines:
    numbers = map(float, line.split())
    sum_sqrt = sum(math.sqrt(num) for num in numbers if num > 0)
    column_results.append(int(sum_sqrt))  # Целая часть от суммы

# Сортировка столбца по убыванию и выбор топ-10 значений
top_10_results = sorted(column_results, reverse=True)[:10]

# Запись результата в файл "задание2/output.txt"
with open('задание2/output.txt', 'w') as output_file:
    for result in top_10_results:
        output_file.write(f"{result}\n")

