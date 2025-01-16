# 2. Дан список чисел, число a и натуральное число k. Выведите индекс k-го по счету
# появления в массиве числа a. Если число a встречается в массиве менее k раз, выведите число
# -1.
# Решение оформите в виде функции KthAppearance(A, a, k).

def KthAppearcance(A,a,k):
    count = 0
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            if count == k:
                return i
    return -1

a = 3
k = 2
A = [1,2,1,3,2,3,2,3,2,2]
с = KthAppearcance(A,a,k)
print(с)