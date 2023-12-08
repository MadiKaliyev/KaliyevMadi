# Задание №2
# Реализуйте программу, чтобы определить, является ли данный год високосным.
import datetime
import math
from datetime import date

def visokosnii(x):
    def wrapper(*args, **kwargs):
        year = args[0]
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return ('ДА')
        else:
            return ('НЕ')
    return wrapper
#
@visokosnii
def visokos(x):
    return x

a = date.today().year
b = visokos(a)
print(f'Сегодняший год {b} високосный! ')




















