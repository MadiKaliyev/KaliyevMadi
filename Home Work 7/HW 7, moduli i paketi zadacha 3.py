# Задание №3.
# Создайте массив 2d с 1 на границе и 0 внутри
import random
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = [[0 for i in range (b)] for i in range (a)]
for i in range(a):
    for j in range(b):
        if i == 0 or i == a - 1 or j == 0 or j == b - 1:
            c[i][j] = 1
for i in c:
    print(i)
#
# a = 6
# b = 4
# c = [["*" for i in range (b)] for i in range (a)]
# for i in range(a):
#     for j in range(b):
#         if i == 0 or i == a - 1 or j == 0 or j == b - 1:
#             c[i][j] = "-"
# for i in c:
#     print(i)

# a = 6
# b = 4
# c = [["*" for i in range (b)] for i in range (a)]
# for i in range(a):
#     for j in range(b):
#         if j == 0 or j == b - 1:
#             c[i][j] = "-"
# for i in c:
#     print(i)
# Или как вариант: если все первые и крайнине будут изменены а центральные нет