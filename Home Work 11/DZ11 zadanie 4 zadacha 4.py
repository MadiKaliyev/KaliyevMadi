# Задание №4
# Напишите программу на Python, чтобы узнать текущее время в Python.
# Format:: 13: 19: 49.078205
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

a = datetime.datetime.now()
print(f'{a:%H:%M:%S}')

a1 = datetime.datetime.now().time()
print(a1)