# Задание №4
# Реализуйте программу, для печати строки пять раз, задержка три секунды.
import time

a = "Привет"
b = 0
while b < 5:
    print(a)
    time.sleep(3)
    b += 1