import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://kaspi.kz/shop/c/smartphones/?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3ASmartphones%3AmanufacturerName%3AApple%3ASmartphones*Series%3AApple%20iPhone%2015%3ASmartphones*Series%3AApple%20iPhone%2015%20Pro%3ASmartphones*Series%3AApple%20iPhone%2015%20Pro%20Max&sort=relevance&sc&page=2')

wait = WebDriverWait(browser, 20)
iphone_prices = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'item-card__prices-price')))

for i in range(len(iphone_prices)):
    if i % 2 == 0:
        print("Цена:", iphone_prices[i].get_attribute('innerText').strip())
