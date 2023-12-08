# Задание №2.
# Реализуйте программу, чтобы найти дату первого понедельника данной недели.
# Date: 2015, 50
# Output: пн 14 декабря 00:00:00 2015
import datetime
import datetime
import math
from datetime import date
from datetime import datetime, timedelta


year, week_number = 2015, 50

a = datetime.strptime(f'{year}-W{week_number}-1', "%Y-W%W-%w")
print(a.strftime("%a %d %B %H:%M:%S %Y"))


