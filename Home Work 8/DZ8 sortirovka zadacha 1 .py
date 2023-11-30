# Домашнее задание №8: Сортировка, поиск, регулярные
# выражения
# При выполнении практической работы, основной алгоритм решения задачи должен быть
# описан в виде функции, получающей в качестве параметра список (а также, возможно, и
# дополнительные параметры).
# 1. Дан список целых чисел. Отсортируйте его в порядке не убывания значений. Выведите
# полученный список на экран.
# Решите эту задачу при помощи алгоритма сортировки вставкой. Решение оформите в
# виде функцииInsertionSort(A).
# В этой задаче нельзя пользоваться дополнительным списком и операциями удаления и
# вставки элементов.
# В алгоритме сортировки вставкой в каждый произвольный момент начальная часть
# списка уже отсортирована. В решении имеется циклfor i in range(1, len(A)), внутри которого в
# предположении, что элементы спискаA[0],A[1], ...,A[i-1]уже отсортированы,
# элементA[i]добавляется в отсортированную часть списка. Для этого находится позиция, в
# которую необходимо вставить элементA[i], затем осуществляется циклический сдвиг
# фрагмента уже отсортированной части.

def InsertionSort(A):
    for i in range(len(A)):
        for j in range(i, 0, -1):
            if A[j] <= A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
a = [1, 4, 2, 3, 4]
InsertionSort(a)
print(a)


