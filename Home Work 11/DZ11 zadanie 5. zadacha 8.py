# Задание №4
# Реализуйте программу на Python, для создания HTML-календаря с данными за
# определенный год и месяц.
import calendar

def create_html_calendar(year, month):
    cal = calendar.HTMLCalendar(calendar.SUNDAY)
    return cal.formatmonth(year, month)

# Пример использования
year_input = int(input("Введите год: "))
month_input = int(input("Введите месяц: "))

calendar_html = create_html_calendar(year_input, month_input)
print(calendar_html)
