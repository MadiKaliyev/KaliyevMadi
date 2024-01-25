# Задание №1
# а) Напишите функцию, которая будет загружать информацию сразу с 100 ссылок.
# б) Запустите эту функцию, а также замерьте время.
# в) Добавьте функционал асинхронного запуска, с замером времени. Обязательно
# посмотрите нагрузку на ЦП в этот момент (через диспетчер задач).

import requests
import time
import asyncio
import aiohttp

def json_request(endpoint):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}{endpoint}"
    response = requests.get(url)
    return response.json()

def fetch_all_sync(endpoints):
    results = []
    for i in endpoints:
        result = json_request(i)
        results.append(result)
    return results

async def json_async(session, endpoint):
    base_url = "https://jsonplaceholder.typicode.com"
    url = f"{base_url}{endpoint}"
    async with session.get(url) as response:
        return await response.json()

async def fetch_all_async(endpoints):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [json_async(session, i) for i in endpoints]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    endpoints = [f"/todos/{i}" for i in range(1, 101)]

    start_time_sync = time.time()
    results_sync = fetch_all_sync(endpoints)
    end_time_sync = time.time()
    print(f"Время выполнения синхронной функции: {end_time_sync - start_time_sync} секунд")

    start_time_async = time.time()
    results_async = asyncio.run(fetch_all_async(endpoints))
    end_time_async = time.time()
    print(f"Время выполнения асинхронной функции: {end_time_async - start_time_async} секунд")
    print(f"Результаты (синхронно):{results_sync}")
    print(f"Результаты (асинхронно):{results_async}")
