from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://mig.kz/'
driver = webdriver.Chrome()
driver.get(url)
kurs = driver.page_source
driver.quit()
soup = BeautifulSoup(kurs, 'html.parser')
usd = soup.find('td', class_='buy delta-neutral')
usd2 = soup.find('td', class_='currency')
usd3 = soup.find('td', class_='sell delta-neutral')
print(f'Покупка: {usd.text} {usd2.text} Продажа {usd3.text}')

table = soup.find('table')
rows = table.find_all('td')
if len(rows) > 3:
    eur = rows[3].get_text(strip=True)
    if len(rows) > 4:
        eur1 = rows[4].get_text(strip=True)
        if len(rows) > 5:
            eur2 = rows[5].get_text(strip=True)
            print(f'Покупка: {eur} {eur1} Продажа {eur2}')
