# Задание №2.
# Напишите функцию, которая проверяет является ли число степенью двойки. Если
# истинно выведите True, иначе False.
def stepen(c):
    if c <= 0:
        return False
    while c > 1:
        if c % 2 != 0:
            return False
        c = c // 2
    return True

a = int(input("Введите число: "))
b = stepen(a)
print(b)