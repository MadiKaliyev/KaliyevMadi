# Задание №1.
# Пользователь вводит с клавиатуры два числа, выполните следующие операции:
# 1. Нужно показать все числа в указанном диапазоне.
# 2. Нужно показать все нечетные числа в указанном диапазоне.
# 3. Нужно показать все четные числа в указанном диапазоне.
# 4. Нужно показать все числа в указанном диапазоне в порядке убывания.

a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))
c = False
if a > b:
    c = True

print(f"Числа в диапазоне от {a} до {b}:")
if not c:
    for i in range(a, b + 1):
        print(i, end=" ")
else:
    for i in range(a, b -1,-1):
        print(i, end=",")

print("\n"f"Все четные числа в диапазоне от {a} до {b}")
if not c:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=",")
else:
    for i in range(a, b - 1,-1):
        if i % 2 == 0:
            print(i, end=",")

print("\n"f"Все не четные числа в диапазоне от {a} до {b}")
if not c:
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=",")
else:
    for i in range(a, b - 1,-1):
        if i % 2 != 0:
            print(i, end=",")

print("\n"f"Числа в диапазоне в порядке убывания от {a} до {b}")
if not c:
    for i in range(b, a - 1, -1):
        print(i, end=",")
else:
    for i in range(b, a + 1):
        print(i, end=",")