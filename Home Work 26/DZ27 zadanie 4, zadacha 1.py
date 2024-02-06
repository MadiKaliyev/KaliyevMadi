# Задание №1
# а) Загрузите одиночный json – объект с сайта jsonplaceholder, используя библиотеку
# requests.
# б) Сохраните его в файл.

import requests
url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url)
if response.status_code == 200:
    json_data = response.json()
    with open('принятые файлы.txt', 'w', encoding='utf-8') as file:
        for i, j in json_data.items():
            file.write(f'{i}:{j}\n')
            print(f'{i}:{j}\n')