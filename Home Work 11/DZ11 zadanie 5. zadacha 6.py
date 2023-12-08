# Задание №2
# Реализуйте программу, для вычисления количества дней между двумя датами

from datetime import datetime

date1 = datetime(2023, 1, 1)
date2 = datetime(2023, 12, 31)

difference = date2 - date1
print("Количество дней между датами:", difference.days)
