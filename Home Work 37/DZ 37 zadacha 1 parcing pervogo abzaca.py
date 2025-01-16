import os
import requests
from bs4 import BeautifulSoup

dir = 'C:/Users/user/Downloads'
os.chdir(dir)

def getText(url):
    content = requests.get(url)
    return content.text

html_doc = getText('https://tengrinews.kz/news/')
soup = BeautifulSoup(html_doc, 'html.parser')
soup.prettify()
news = soup.find('span', class_='content_main_item_title')
istochnik = 'https://tengrinews.kz/' + news.a['href']

html_doc2 = getText(istochnik)
soup2 = BeautifulSoup(html_doc2, 'html.parser')

news2 = soup2.find('div', class_='content_main_text')
abzac2 = news2.find_all('p')
if len(abzac2) > 1:
    print(f'\nАбзац методом BeautifulSoup:{abzac2[1].get_text()}\n')

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://tengrinews.kz/news/')
block = browser.find_element(By.CLASS_NAME, 'content_main_item_title')
block.click()

novost = browser.find_element(By.CLASS_NAME, 'content_main_text')
inner_text = novost.text
abzac2 = novost.find_elements(By.TAG_NAME, 'p')
if len(abzac2) > 1:
    print(f'Абзац методом Selenium:{abzac2[1].text}')
