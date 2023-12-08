# Задание №3
# Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и
# секунды


from datetime import timedelta

a1 = timedelta(days=5, hours=3, minutes=20, seconds=10)
b1 = timedelta(days=2, hours=15, minutes=45, seconds=30)

c = a1 + b1

days = c.days
hours, c1 = divmod(c.seconds, 3600)
minutes, seconds = divmod(c1, 60)

print("Разность дат в виде: {} дней, {} часов, {} минут, {} секунд".format(days, hours, minutes, seconds))
