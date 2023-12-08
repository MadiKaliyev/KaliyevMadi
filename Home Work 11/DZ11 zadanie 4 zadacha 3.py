# Задание №3
# Реализуйте программу, для преобразования строки в дату и время.
# Input: 1 января 2014 14:43
# Output: 2014-07-01 14:43:00
import datetime
from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
months = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}
a = '1 декабрь 2014 14:43'
b = datetime.datetime.strptime(a, '%d %B %Y %H:%M')
print(b.strftime('%d %B %Y %H:%M'))