# Задание №1.
# Реализуйте программу, чтобы получить номер недели.
# Date: 2015, 6, 16
# Output: 25
import datetime

data = "2015, 6, 16"
a = datetime.datetime.strptime(data, '%Y, %m, %d')
print(a.strftime('%W'))

