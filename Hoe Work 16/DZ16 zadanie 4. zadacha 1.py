# Задание №1.
# Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно из
# них не является числом, то должна выполняться конкатенация, то есть соединение, строк. В
# остальных случаях введенные числа суммируются.

a = input("Введите а: ")
b = input("Введите b: ")

try:
    summ = float(a)+float(b)
    print(summ)
except ValueError:
    print(a+b)