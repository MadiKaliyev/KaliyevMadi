# Задание №1
# а) Загрузите массив json – объектов с сайта jsonplaceholder, используя библиотеку
# aiohttp.
# б) Сохраните циклом каждый в отдельный файл, в одну новую папку
import aiohttp
import asyncio
import os

async def data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()
                output_folder = 'Посты'
                os.makedirs(output_folder, exist_ok=True)

                for post in json_data:
                    user_id = post["userId"]
                    title = post['title']
                    body = post['body']
                    post_id = post['id']
                    user_folder = os.path.join(output_folder, f'Пользователь_{user_id}')
                    os.makedirs(user_folder, exist_ok=True)

                    file_name = f'Пост_{post_id}.txt'
                    file_path = os.path.join(user_folder, file_name)

                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(f'User ID: {user_id}\nTitle: {title}\nBody: {body}\n')
                        print(f'User ID: {user_id}\nTitle: {title}\nBody: {body}\n')

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(data())