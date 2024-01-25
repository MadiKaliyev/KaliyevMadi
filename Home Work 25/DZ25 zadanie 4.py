# Задание №1
# а) Напишите функцию, которая будет загружать данные с jsonplaceholder.
# б) Запустите циклом 100 таких функций, а также замерьте время.
# в) Добавьте функционал асинхронной работы, с замером времени
import time
import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

def get_json(endpoint):
    base = "https://jsonplaceholder.typicode.com"
    url = f"{base}{endpoint}"
    zapros = requests.get(url)
    return zapros.json()

start_time = time.time()

for i in range(100):
    data = get_json('/posts')
    if data:
        print(data)

end_time = time.time()
obchii_time = end_time - start_time
print(f"Время выполнения для 100 синхронных запросов: {obchii_time:.2f} секунд")


async def main():
    async with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        tasks = [loop.run_in_executor(executor, get_json, '/posts') for _ in range(100)]
        results = await asyncio.gather(*tasks)

        for data in results:
            if data:
                print(data)

start_time = time.time()
asyncio.run(main())
end_time = time.time()
obchii_time = end_time - start_time
print(f"Время выполнения для 100 асинхронных запросов: {obchii_time:.2f} секунд")

