# Задание №4.
# Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить
# новую дату.
# Example: (addYears - это имя пользовательской функции)
# print (addYears (datetime.date (2015,1,1), -1))
# print (addYears (datetime.date (2015,1,1), 0))
# print (addYears (datetime.date (2015,1,1), 2))
# печати (addYears (datetime.date (2000,2,29), 1))
# Output:
# 2014-01-01
# 2015-01-01
# 2017-01-01
# 2001-03-01
import datetime

import datetime
import datetime
def years(x1,x2):
    data = datetime.datetime.strptime(x1, '%Y %m %d')

    if b > 0:
        new_date = data.replace(year=data.year + x2)
        print(f'{new_date:%Y-%m-%d}')
    else:
        new_date = data.replace(year=data.year - abs(b))
        print(f'{new_date:%Y-%m-%d}')


a = input("Введите дату через пробел: ")
b = int(input("Выберите сколько лет нужно прибавить или отнять: "))
c = years(a,b)

