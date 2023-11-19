# Задание № 1.
# Напишите функцию вычисления (), которая может принимать две переменные и
# вычислять сложение и вычитание. Результат функции должен возвращаться в одном
# обратном вызове.
# Input
# Enter two numbers in one line: 55 6
# Output
# The sum of numbers is 61, the difference of numbers is 49.
# import math
def slozhenie(a, b):
    if a > b:
        print(a + b, a - b)
    else:
        print(b + a, b - a)
a = int(input("a: "))
b = int(input("b: "))
slozhenie(a, b)