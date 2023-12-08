# Задание №4
# Реализуйте программу на Python, для создания HTML-календаря с данными за
# определенный год и месяц.
import calendar

def html(year, month):
    x = calendar.HTMLCalendar(calendar.SUNDAY)
    return x.formatmonth(year, month)

god = int(input("Введите год: "))
mesyac = int(input("Введите месяц: "))

a = html(god, mesyac)
print(a)
