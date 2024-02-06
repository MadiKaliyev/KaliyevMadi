# Задание №1
# а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку
# requests.
# б) Сохраните циклом каждый в отдельный файл, в одну новую папку.
# В качестве ответа прикрепить скрин и ссылку на github.

import requests
import os

output_folder = 'Юзеры'
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

if response.status_code == 200:
    json_data = response.json()

    os.makedirs(output_folder, exist_ok=True)

    for post in json_data:
        user_id = post["userId"]
        title = post['title']
        body = post['body']
        id = post['id']

        user_folder = os.path.join(output_folder, f'Пользователь_{user_id}')
        os.makedirs(user_folder, exist_ok=True)

        file_name = f'Кто то_{post["id"]}.txt'
        file_path = os.path.join(user_folder, file_name)

        with open(file_path, 'w') as file:
            file.write(f"User ID: {user_id}\nTitle: {title}\nBody: {body}\nid: {id}\n")


