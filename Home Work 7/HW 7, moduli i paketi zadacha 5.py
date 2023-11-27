# Задание №5.
# Как получить все даты, соответствующие определенному месяцу и году август 2022?
import datetime

year = 2000
month = 2

data = datetime.date(year, month, 1)
konec = datetime.date(year, month + 1, 1) if month < 12 else datetime.date(year + 1, 1, 1)

dates_list = []

a = data
while a < konec:
    dates_list.append(a)
    a += datetime.timedelta(days=1)

for data in dates_list:
    print(data)
