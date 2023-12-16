# Задание №1
# а) Создайте json файл в операционной системе, заполните его данными с сайта
# https://jsonplaceholder.typicode.com/todos/
# б) Прочитайте этот файл в массив python-словарей.
# в) Запишите каждый из этих словарей в отдельный json-файл.
import random
import string
import json
import json

with open('fail.json', encoding='utf-8') as fail_json:
  data = json.load(fail_json)
  data_list = [data]
print(data_list)





