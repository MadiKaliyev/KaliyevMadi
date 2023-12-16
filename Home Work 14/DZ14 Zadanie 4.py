# Задание №1
# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/1
# б) Прочитайте этот файл в python-словарь.
# в) Сгенерируйте 100 словарей и запишите их в один json-файл
import random
import string
import json

with open('fail.json', encoding='utf-8') as fail_json:
  data = json.load(fail_json)

for i, j in data.items():
  print(i, j)