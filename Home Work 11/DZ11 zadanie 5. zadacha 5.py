# Задание №1
# Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
#


from datetime import datetime, timezone

a = datetime.now(timezone.utc)
print("Время по Гринвичу:", a)

b = datetime.now()
print("Местное время:", b)
