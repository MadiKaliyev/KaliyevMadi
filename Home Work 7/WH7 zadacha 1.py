# Задание №1.
# Написать лямбду-функцию, которая:
# 1. добавляет 15 к заданному числу, переданному в качестве аргумента;
# Input: 10 Output:25
# 2. умножает аргумент x на аргумент y, выведите результат;
# Input: 12 4 Output:48
# 3. фильтрует список целых чисел, заданных пользователем;
# Список целых чисел:
# [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
# Список четных чисел:
# [78, 2, 46, 74, 94, 10]
# Список нечетных чисел:
# [13, 5, 61, 81]
# 4.выводит год, месяц, дату и время.
# При решении используйте модуль datetime. Output:
# 2022-07-19 07:58:31.246609
# 2022
# 7
# 19
# 07:58:31.246609
import datetime
#
a = int(input("Введите число: "))
print((lambda x: x + 15)(a))

a1 = int(input("Введите число: "))
b1 = int(input("Введите число: "))
print((lambda x1, x2: x1 * x2)(a1, b1))

a2 = list(map(int, input("Введите список через пробел: ").split()))
chet = filter(lambda x: x % 2 == 0, a2)
nechet = filter(lambda x: x % 2 != 0, a2)

print("Заданные числа","", a2, "\nЧетные числа:"," ", chet)
print("Нечетные числа:", nechet)

a3 = datetime.datetime.now()
b3 = a3.time()
print(a3)


