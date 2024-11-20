import csv

# Загрузка данных из файла
with open('fourth_task.txt', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Удаляем столбец "expiration_date" и фильтруем по статусу "Pending"
filtered_data = []
for row in data:
    if row['status'] == 'Pending':
        del row['expiration_date']
        filtered_data.append(row)

# Преобразуем числовые значения
for row in filtered_data:
    row['price'] = float(row['price'])
    row['quantity'] = int(row['quantity'])

# Вычисления
avg_price = sum(row['price'] for row in filtered_data) / len(filtered_data) if filtered_data else 0
max_price = max(row['price'] for row in filtered_data) if filtered_data else 0
min_quantity = min(row['quantity'] for row in filtered_data) if filtered_data else 0

with open('задание4/results.txt', 'w', encoding='utf-8') as results_file:
    results_file.write("%.2f\n" % avg_price)  # Среднее по price
    results_file.write("%.2f\n" % max_price)  # Максимум по price
    results_file.write("%d\n" % min_quantity)  # Минимум по quantity

with open('задание4/modified_data.csv', 'w', encoding='utf-8', newline='') as modified_file:
    fieldnames = list(filtered_data[0].keys())  # Заголовки столбцов после удаления expiration_date
    writer = csv.DictWriter(modified_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_data)

