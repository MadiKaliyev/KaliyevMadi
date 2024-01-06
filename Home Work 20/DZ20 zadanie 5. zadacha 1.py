# # Задание №1
# # Создайте класс Circle (окружность). Для данного класса реализуйте ряд перегруженных
# # операторов:
# # Проверка на равенство радиусов двух окружностей (операция = =);
# # Сравнения длин двух окружностей (операции >, <, <=,>=);
# # Пропорциональное изменение размеров окружности, путем изменения ее радиуса
# # (операции + - += -=).
import math

class Circle:
    def __init__(self, r):
        self.r = r

    def __eq__(self, other):
        return self.r == other.r

    def __gt__(self, other):
        return self.r > other.r

    def __lt__(self, other):
        return self.r < other.r

    def __ge__(self, other):
        return self.r >= other.r

    def __le__(self, other):
        return self.r <= other.r

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.r + other.r)
        else:
            return Circle(self.r + other)

    def __sub__(self, other):
        if isinstance(other, Circle):
            return Circle(self.r - other.r)
        else:
            return Circle(self.r - other)

    def __iadd__(self, other):
        self.r += other
        return self

    def __isub__(self, other):
        self.r -= other
        return self

circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)
print(circle1 < circle2)
circle3 = circle1 + circle2
print(circle3.r)
print((circle1 + 2).r)
print((circle1 - 3).r)
circle1 += 3
print(circle1.r)
