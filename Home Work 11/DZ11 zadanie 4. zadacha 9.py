# Задание №5
# Реализуйте программу, чтобы получить даты за 30 дней до и после текущей даты
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import calendar
from datetime import datetime
from datetime import datetime, timedelta




a = datetime.now()
b = a - timedelta(days=30)
c = a + timedelta(days=30)
print(f'30 дней до сегодня {b:%Y %m %d}')
print(f'сегодня {a:%Y %m %d}')
print(f'30 дней после сегодня {c:%Y %m %d}')