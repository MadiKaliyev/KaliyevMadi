import random
# 2. Дан список целых чисел. Выведите все элементы этого списка в порядке не возрастания
# значений. Выведите новый список на экран.
# Решите эту задачу при помощи алгоритма сортировки выбором. Решение оформите в
# виде функции SelectionSort(A).
# В алгоритме сортировки выбором мы находим наибольший элемент в списке и ставим его
# на первое место, затем находим наибольший элемент из оставшихся и ставим его на второе
# место и т.д.
# В этой задаче разрешается модифицировать исходный список, в частности, удалить из
# списка i-й элемент можно при помощи метода pop(i), и использовать новый список для
# добавления в него элементов.

# def SelectionSort(a):
#     for i in range(len(a)):
#         for j in range(i):
#             if a[j] <= a[i]:
#                 a[j], a[i] = a[i], a[j]
#
# a = [1, 4, 2, 3, 4]
# SelectionSort(a)
# print(a)
#
# Решил по баловаться )))))

# def SelectionSort(a):
#     for i in range(len(a)):
#         for j in range(i):
#             if a[j] <= a[i]:
#                 a[j], a[i] = a[i], a[j]


# a = [random.randint(1,100)for i in range(100)]
# SelectionSort(a)
# print(a)

# def SelectionSort(a):
#     for i in range(len(a)):
#         for j in range(i):
#             if a[j] <= a[i]:
#                 a[j], a[i] = a[i], a[j]
# import random
# b = int(input("Введите число: "))
# a = [random.randint(1, b)for i in range(b)]
# SelectionSort(a)
# print(a)