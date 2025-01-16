# Задание №4.
# Создайте матрицу 5x5 со значениями 1,2,3,4 чуть ниже диагонали.
import random
# a = [[1,2,3,4,5]for i in range(5)]
# for i in a:
#     print(i)

# Еще вариант.
# a = [['*' for i in range(5)] for j in range(5)]
# for i in a:
#     for j in a:
#       if i == 1 and j == 1:
#         a[i][j] = 1
#
#     print(' '.join(i))
# a = [['*' if j != i - 1 else str(i) for j in range(0, 5)] for i in range(5)]
# for i in a:
#     print(i)
