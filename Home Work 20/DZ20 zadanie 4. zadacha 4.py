# Задания №4
# Создайте класс Date, который будет содержать информацию о дате (день, месяц, год). С
# помощью механизма перегрузки операторов, определите операцию разности двух дат
# (результат в виде количества дней между датами), а также операцию увеличения даты на
# определенное количество дней.
from datetime import timedelta, datetime


class Date:
    def __init__(self, day, month, year):
        self.date = datetime(year, month, day)

    def __sub__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Operand must be of type 'Date'")

        return abs((self.date - other.date).days)

    def add_days(self, days):
        self.date += timedelta(days=days)
        return self.date.strftime("%d-%m-%Y")


# Пример использования
date1 = Date(1, 1, 2019)
date2 = Date(1, 1, 2020)

difference = date1 - date2
print(f"Количество дней между датами: {difference}")

new_date = date1.add_days(100)
print(f"Новая дата после добавления 100 дней: {new_date}")






