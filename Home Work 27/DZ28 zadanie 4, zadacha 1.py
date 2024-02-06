# Задание №1
# а) Загрузите одиночный json – объект с сайта jsonplaceholder, используя библиотеку
# aiohttp.
# б) Сохраните его в файл.
import aiohttp
import asyncio

async def data():
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()
                with open('принятые файлы.txt', 'w', encoding='utf-8') as file:
                    for key, value in json_data.items():
                        file.write(f'{key}:{value}\n')
                        print(f'{key}:{value}\n')
            else:
                print("Ошибка при запросе:", response.status)



