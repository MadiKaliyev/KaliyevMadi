# Задание №1
# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/1
# б) Прочитайте этот файл в python-словарь.
# в) Сгенерируйте 100 словарей и запишите их в один json-файл

import json
import random
import string

def imya():
    letters = string.ascii_lowercase
    for i in range(100):
        dlinna = random.randint(3,10)
        return ''.join(random.choice(letters) for _ in range(dlinna))

list_of_dicts = []
for _ in range(100):
    new_dict = {
        "имя:": imya(),
        "возраст:": random.randint(18, 60),
        "город:": random.choice(["Алматы", "Астана", "Шымкент", "Актау"]),
        "Образование:": random.choice(["Высшее", "Среднее", "Среднее специальное", "Среднее профессиональне"]),
        "Политичесие взгляды:": random.choice(["Консерватор", "Либерал", "Либертарианец", "Тоталитарист"]),
        "хобби:": ','.join(random.sample(["чтение", "спорт", "путешествия", "готовка","Шахматы","Лыжи","Баня"], random.randint(1, 6)))
    }
    list_of_dicts.append(new_dict)

with open('словари.json', 'w', encoding='utf-8') as file:
    json.dump(list_of_dicts, file, ensure_ascii=False, indent=1)

with open('словари.json', encoding='utf-8') as fail_json:
  data = json.load(fail_json)
for i in data:
  for key, value in i.items():
    print(f'{key} {value}')
  print('')