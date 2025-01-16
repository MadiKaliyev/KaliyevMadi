# Задание № 2.
# Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1,
# x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре
# действительных числа и выведите результат работы этой функции. Используйте теорему
# Пифагора.

def distance(x1, y1, x2, y2):
    a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return a
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
a = distance(x1, y1, x2, y2)
print("Расстояние между точками:", a)