# Домашнее задание №10: Итераторы, контейнеры и перечисления
# Выполните следующее задание:
# Создать генератор списка из исходного, который:
import re
import random
import math

# a1 = [1, 2, 3, 4, 5, 6, 7]
# a2 = {i: i**3 for i in a1 if i % 2 != 0}
# a3 = {i for i in a1 if i % 2 == 0}
# a4 = [i*10 for i in range(0,10)]
# print(a1)
# print(a2)
# print(a3)
# print(a4)
#
def delenie(x):
    for i in x:
        if i % 7 == 0:
            yield i

a = [random.randint(0,100)for i in range(20)]
print(a)
for i in delenie(a):
    print(i, end=" ")
