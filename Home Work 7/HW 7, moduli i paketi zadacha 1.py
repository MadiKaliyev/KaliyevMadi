# Задание №1.
# Напишите программу, в которой необходимо создать массив 10x10 со случайными
# значениями и найдите минимальное и максимальное значения.

import random
a = [[random.randint(0, 99) for i in range(10)] for i in range (10)]
minimum = min(map(min, a))
maximum = max(map(max, a))

for i in a:
    print(i)
print(f"Максимум {maximum}\nМинимум  {minimum}")


