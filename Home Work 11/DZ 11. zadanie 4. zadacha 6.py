# Задание №2
# Реализуйте программу, чтобы узнать количество дней в данном месяце и году.

import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import calendar


a = int(input("Введите год: "))
b = int(input("Введите месяц: "))
year = a
if calendar.isleap(year):
    print(f'Количество дней в заданном году {366}')
else:
    print(f'Количество дней в заданном году {365}')
days_in_month = calendar.monthrange(a, b)[1]
print(f'Количество дней в заданном месяце: {days_in_month}')


