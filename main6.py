import requests

def fetch_weather(city):
    try:
        response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Failed to fetch weather for {city}. Error: {e}"

cities = ["Moscow", "Yekaterinburg", "Izhevsk", "Sochi"]
html_content = """<html>
<head><title>Данные о погоде</title></head>
<body>
<h1>Погода в городах</h1>
<table border="1">
<tr>
    <th>Город</th>
    <th>Погода</th>
</tr>
"""

for city in cities:
    weather = fetch_weather(city)
    html_content += f"<tr><td>{city}</td><td>{weather}</td></tr>\n"

html_content += """
</table>
</body>
</html>
"""

# Записываем результат в файл
with open("задание6/weather.html", "w", encoding="utf-8") as file:
    file.write(html_content)