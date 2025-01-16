# Задание №1
# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/
# б) Прочитайте этот файл в массив python-словарей.
# в) Запишите каждый из этих словарей в отдельный json-файл.
import random
import string
import json
import json

with open('словари.json', encoding='utf-8') as fail_json:
  data_list = json.load(fail_json)
for i, dictionary in enumerate(data_list, start=1):
    filename = f'dict_{i}.json'
    with open(filename, 'w') as file:
        json.dump(dictionary, file, indent=1)
print()