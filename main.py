import re
from collections import Counter

# Загрузка текста из файла
with open('first_task.txt', 'r') as file:
    text = file.read()

# Удаляем пунктуацию, приводим текст к нижнему регистру и оставляем только слова, состоящие из букв
# учитываем что i'am и it's одно слово
words = re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]+(?:'[a-z]+)?\b", text.lower())
word_count = Counter(words)

# Подсчет среднего количества слов в предложениях
sentences = re.split(r'[.!?]', text)
sentences = [s.strip() for s in sentences if s]
average_words = sum(len(re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]+(?:'[a-z]+)?\b", s)) for s in sentences) / len(sentences)

with open('задание1/word_frequency.txt', 'w', encoding='utf-8') as wf:
    for word, freq in word_count.most_common():
        wf.write(f"{word}:{freq}\n")

with open('задание1/average_words_per_sentence.txt', 'w', encoding='utf-8') as af:
    af.write(f"Среднее количество слов в предложении: {average_words:.2f}\n")
