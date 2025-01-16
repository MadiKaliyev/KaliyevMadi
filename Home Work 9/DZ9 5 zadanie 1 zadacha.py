# Домашнее задание №9: Сортировка, поиск, регулярные
# выражения
# При выполнении практической работы, основной алгоритм решения задачи должен быть
# описан в виде функции, получающей в качестве параметра список (а также, возможно, и
# дополнительные параметры).
# 1. Заданы M строк символов, которые вводятся с клавиатуры. Найти количество
# символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив
# перед каждой строкой соответствующее количество звёздочек.

a = int(input("Введите количество строк "))
zv = '*'
maximalnii = 0
stroki = []
new_stroki = []

for i in range(a):
    stroka = input("Введите строку ")
    stroki.append(stroka)

for i in stroki:
    dlinna = len(i)
    if dlinna > maximalnii:
        maximalnii = dlinna

for i in stroki:
    if len(i) == maximalnii:
        new_stroki.append(i)
    else:
        i = zv * (maximalnii - len(i)) + i
        new_stroki.append(i)

for i in new_stroki:
    print(i)
