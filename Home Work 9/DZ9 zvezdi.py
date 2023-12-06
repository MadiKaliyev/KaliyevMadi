# Домашнее задание №9: Сортировка, поиск, регулярные
# выражения
# При выполнении практической работы, основной алгоритм решения задачи должен быть
# описан в виде функции, получающей в качестве параметра список (а также, возможно, и
# дополнительные параметры).
# 1. Заданы M строк символов, которые вводятся с клавиатуры. Найти количество
# символов в самой длинной строке. Выровнять строки по самой длинной строке, поставив
# перед каждой строкой соответствующее количество звёздочек.
def zvezdi(x):
    dlinna = max(len(i) for i in x)
    for s in x:
        c = dlinna - len(s)
        stars = '*' * c
        print(stars + s)


a = ['da', 'net', 'poka']
b = zvezdi(a)
