# Задание №3
# Реализуйте программу, для преобразования двух разностей дат в дни, часы, минуты и
# секунды


from datetime import timedelta

difference1 = timedelta(days=5, hours=3, minutes=20, seconds=10)
difference2 = timedelta(days=2, hours=15, minutes=45, seconds=30)

total_difference = difference1 + difference2

days = total_difference.days
hours, remainder = divmod(total_difference.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print("Разность дат в виде: {} дней, {} часов, {} минут, {} секунд".format(days, hours, minutes, seconds))
