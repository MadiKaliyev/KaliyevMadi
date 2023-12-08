# Задание №3.
# Реализуйте программу, чтобы выбрать все воскресенья определенного года.
import datetime
import datetime
import math
from datetime import date
from datetime import datetime, timedelta

year = 2015

PN = [datetime(year, 1, 1) + timedelta(days=i) for i in range(365) if (datetime(year, 1, 1) + timedelta(days=i)).weekday() == 6]

for i in PN:
    print(i.strftime('%Y-%m-%d'))