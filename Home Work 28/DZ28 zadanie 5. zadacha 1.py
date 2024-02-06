# Задание №1
# а) Загрузите циклом 10 рандомных картинок с сайта используя библиотеку requests,
# затем aiohttp.
# б) Сохраните их в разные папки циклом.
import asyncio
import os

import aiohttp
import requests
from io import BytesIO
from PIL import Image

for _ in range(10):
    width = 400
    height = 300

    url = f'https://picsum.photos/{width}/{height}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))

        filename = f'random_image_{_ + 1}.jpg'
        image.save(filename)
        print(f'Фотки {_ + 1} сохранено: {filename}')

    except requests.RequestException as e:
        print(e)

async def fetch_and_save_image(session, url, folder_name, index):
    async with session.get(url) as response:
        response.raise_for_status()
        image_content = await response.read()

        image = Image.open(BytesIO(image_content))
        filename = f'{folder_name}/random_image_{index + 1}.jpg'
        image.save(filename)
        print(f'Фото {index + 1} сохранено: {filename}')

async def main():
    width = 400
    height = 300

    for i in range(10):
        url = f'https://picsum.photos/{width}/{height}'
        folder_name = f'images_{i + 1}'

        try:
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)

            async with aiohttp.ClientSession() as session:
                await fetch_and_save_image(session, url, folder_name, i)

        except requests.RequestException as e:
            print(e)

if __name__ == "__main__":
    asyncio.run(main())