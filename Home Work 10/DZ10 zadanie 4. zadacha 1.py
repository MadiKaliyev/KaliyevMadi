# Практическая работа №10: Итераторы, контейнеры и
# перечисления
# Выполните следующие задания:
# Создать генератор списка из исходного, который:
# 1.берет только четные значения, отрицательные возводит в куб, остальные в квадрат
# 2. считает длину строк для списка из строк
# 3. список квадратов четных чисел
# 4. только положительные, кратные 5, отрицательные заменить на 0
# 5. из строки – только гласные буквы.
import re
import random
import math

def list(x):
    x1 = [x ** 3 if x < 0 else x ** 2 if x % 2 == 0 else x for x in x]
    print(x1)

def list2(x):
    x1 = [len(string) for string in x]
    print(x1)

def list3(x):
    x1 = [x ** 2 for x in x if x % 2 == 0]
    print(x1)

def list4(x):
    x1 = [x if x > 0 and x % 5 == 0 else 0 if x < 0 else x for x in x]
    print(x1)

def list5(x):
    x1 = [i for word in x for i in word if i.lower() in 'aeiouAEIOUаяуюоеёэиыАЯУЮОЕЁЭИЫ']
    print(x1)

a = [random.randint(-20,20)for i in range(10)]
print(f'начальный список:{a}')
b = list(a)
b2 = list3(a)
b3 = list4(a)

a1 = input("Введите текст: ").split()
b1 = list2(a1)
b4 = list5(a1)






# def raschet(a):
#     b = []
#     c = []
#     d = []
#     e = []
#     chet_kvadtat = []
#     for i in range(len(a)):
#         if a[i] < 0:
#             a[i] = a[i]**3
#             b.append(a[i])
#             a[i] = a[i] = 0
#             a.append(a[i])
#         elif a[i] % 2 == 0:
#             chet_kvadtat.append(a[i]**2)
#             c.append(a[i])
#         elif a[i] > 0 and a[i] % 5 == 0:
#             e.append(a[i])
#         else:
#             a[i] = a[i]**2
#             d.append(a[i])
#     print(f'отрицательные значения возведенные в куб: {b}')
#     print(f'Четные значения: {c}')
#     print(f'Остальные значения возведенные в квадрат: {d}')
#     print(f'Четные числа в квадрате: {chet_kvadtat}')
#     print(f'Положительные числа и кратные пяти: {e}')
#     print(f'Замена отрицательных чисел на ноль: {a}')
# def podschet(x):
#     x1 = []
#     for i in range(len(x)):
#         x1.append(len(x[i]))
#     print(x1)
#     x2 = []
#     slova = ' '.join(x)
#     glasnie = "aeiouAEIOUаяуюоеёэиыАЯУЮОЕЁЭИЫ"
#     bukvi = [i for i in slova if i in glasnie]
#     x2.append(bukvi)
#     print(f'Все гласные буквы: {x2[0]}')
#
# a = [random.randint(-20,20)for i in range(10)]
# print(f'начальный список:{a}')
# b = raschet(a)
# c = input("Введите текст: ").split()
# d = podschet(c)


