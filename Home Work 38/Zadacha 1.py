import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def iphone15():
    prices = []
    for i in range(24):
        browser = webdriver.Chrome()
        browser.get('https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-seryi-113138420/?c=750000000')
        wait = WebDriverWait(browser, 10)
        iphone = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'item__price-once')))
        prices.append(iphone.text)
        time.sleep(3600)
    return prices

a = iphone15()
for i in a:
    print("Цена: " + i)

