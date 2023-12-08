# Задание №1
# Реализуйте программу, чтобы узнать время по Гринвичу и местное время.
#


from datetime import datetime, timezone

# Время по Гринвичу
gmt_time = datetime.now(timezone.utc)
print("Время по Гринвичу:", gmt_time)

# Местное время
local_time = datetime.now()
print("Местное время:", local_time)
