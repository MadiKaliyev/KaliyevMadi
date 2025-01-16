# Задание №1.
# Написать рекурсивную функцию, которая по заданному целому числу возвращает n-e
# число Фибоначчи. Ряд Фибоначчи 0, 1, 1, 2, 3, 5, 8, 13,……
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n - 2)
def fibo2(n):
    for i in range(1, n+1):
        itog = fibo(i)
        print(f"Число Фибоначчи под номером {i} равно {itog}")

a = int(input("Введите число: "))
c = fibo2(a)