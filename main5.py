import csv

# Чтение HTML-файла
with open('fifth_task.html', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Рекурсивный парсинг узлов
def parse_html(lines, start_tag, end_tag):
    """Парсинг содержимого между тегами start_tag и end_tag"""
    in_tag = False
    content = []
    for line in lines:
        if start_tag in line:
            in_tag = True
            continue
        if end_tag in line:
            in_tag = False
            break
        if in_tag:
            content.append(line.strip())
    return content

# Извлечение заголовков из <thead>
thead = parse_html(lines, '<thead>', '</thead>')
headers = []
for line in thead:
    if '<th' in line:
        headers.append(line.split('>')[1].split('<')[0])

# Извлечение строк из <tbody>
tbody = parse_html(lines, '<tbody>', '</tbody>')
rows = []
for line in tbody:
    if '<tr>' in line:
        row = []
    elif '<td' in line:
        row.append(line.split('>')[1].split('<')[0])
    elif '</tr>' in line:
        rows.append(row)

# Запись в CSV
csv_file = 'задание5/products.csv'
with open(csv_file, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Заголовки
    writer.writerows(rows)    # Данные