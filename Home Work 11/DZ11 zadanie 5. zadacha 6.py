# Задание №2
# Реализуйте программу, для вычисления количества дней между двумя датами

from datetime import datetime

a = datetime(2023, 1, 1)
b = datetime(2023, 12, 31)

c = b - a
print("Количество дней между датами:", c.days)