import os
import requests
from bs4 import BeautifulSoup

dir = 'C:/Users/user/Downloads'
os.chdir(dir)

def getWeather(url):
    content = requests.get(url)
    return content.text

html_doc = getWeather('https://yandex.kz/pogoda/astana')
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()

date_time = soup.find('time', class_='time fact__time')
date_temp = soup.find('span', class_='temp__value temp__value_with-unit')
data_city = soup.find('h1', class_='title title_level_1 header-title__title', id='main_title')

print(data_city.get_text(),': температура сейчас:', date_temp.get_text(), f'\nВремя {date_time.text}')



