# Задание №2.
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит
# из чисел от 1 до i без пробелов.
n = int(input("Введите число n: "))
if n >= 1 and n <= 9:
    for i in range(1, n + 1):
        a = ""
        for j in range(1, i + 1):
            a += str(j)
        print(a)
else:
    print("Введите число от 1 до 9")

