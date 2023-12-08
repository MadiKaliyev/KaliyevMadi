# Задание №1
# Реализуйте программу, чтобы получить последний день указанного года и месяца.

import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import calendar

a = input("Введите дату через пробел: ").split()
b, c = map(int, a)
last_day = calendar.monthrange(b, c)[1]
print(last_day)

