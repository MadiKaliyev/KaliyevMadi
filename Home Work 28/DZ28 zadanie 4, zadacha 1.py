# а) Загрузите одиночную html страницу с сайта википедии, используя библиотеку
# requests, затем aiohttp.
# б) Сохраните оба раза её в файл.

import requests
import aiohttp
import asyncio

url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

try:
    response = requests.get(url)
    response.raise_for_status()

    if response.status_code == 200:
        html = response.text
        with open('wiki_request.txt', 'w', encoding='utf-8') as file:
            file.write(html)
            print(html)

except requests.RequestException as e:
    print(e)

async def fetch_html(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()

async def main():
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    html = await fetch_html(url)

    with open('wiki_asinh.txt', 'w', encoding='utf-8') as file:
        file.write(html)
        print(html)

if __name__ == "__main__":
    asyncio.run(main())
