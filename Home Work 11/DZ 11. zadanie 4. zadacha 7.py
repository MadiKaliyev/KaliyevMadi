# Задание №3
# Реализуйте программу, для подсчета числа понедельника 1-го числа месяца с 2015 по
# 2016 год.

import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import calendar
from datetime import datetime


pn = 0
for i in range(2015, 2017):
    for j in range(1, 13):
        dni = calendar.weekday(i, j, 1)
        if dni == 0:
            pn += 1
print(pn)