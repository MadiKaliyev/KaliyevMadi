import datetime
from datetime import date


# Выполните следующие задания:
# Задание №1.
# Реализуйте программу для отображения различных форматов даты и времени.
# а) текущая дата и время
# б) текущий год
# в) месяц года
# г) номер недели в году
# д) будний день недели
# е) день года
# г) день месяца
# з) день недели

a = datetime.datetime.now()
if a.weekday() < 5:
    b = "Будний"
else:
    b = "Выходной"
print(f'{a:%d.%m.%Y %H:%M:%S}\n{a:%Y}\n{a:%B}\n{a:%W}\n{b}\n{a:%j}\n{a:%d}\n{a:%w}')

# a = datetime.datetime.now()
# b = a.weekday()
# dni = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# dni2 = dni[b]
# den_goda = a.strftime("%j")
# den_mesyaca = a.strftime("%d")
#
# print(f"Текущая дата и время: {a}")
# print(f"Текущий год: {a.year}")
# print(f"Текущий месяц: {a.month}")
# print(f"Номер недели в году: {a.isocalendar()[1]}")
# print(f"Будний день недели: {dni2}")
# print(f"День года: {den_goda}")
# print(f"День месяца: {den_mesyaca}")
# print(f"День недели: {a.weekday()}")