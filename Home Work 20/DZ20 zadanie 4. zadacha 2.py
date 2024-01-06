# Создайте класс Дробь (или используйте уже ранее созданный вами). Используя
# перегрузку операторов реализуйте для него арифметические операции для работы с дробями
# (операции +, -, *, /).

class Drob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def sokrachenie(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __add__(self, other):
        x1 = self.x * other.y + other.x * self.y
        x2 = self.y * other.y
        x3 = self.sokrachenie(x1, x2)
        return Drob(x1//x3, x2//x3)

    def __sub__(self, other):
        if self.x * other.y > other.x * self.y:
            x1 = self.x * other.y - other.x * self.y
            x2 = self.y * other.y
            return Drob(x1, x2)
        else:
            x1 = other.x * self.y - self.x * other.y
            x2 = self.y * other.y
        x3 = self.sokrachenie(x1, x2)
        return Drob(x1//x3, x2//x3)

    def __mul__(self, other):
        x1 = self.x * other.x
        x2 = self.y * other.y
        x3 = self.sokrachenie(x1, x2)
        return Drob(x1 // x3, x2 // x3)

    def __truediv__(self, other):
        x1 = self.x * other.y
        x2 = self.y * other.x
        x3 = self.sokrachenie(x1, x2)
        return Drob(x1//x3, x2//x3)

    def result(self):
        print(f'{self.x}/{self.y}')

a = Drob(1, 4)
b = Drob(1, 2)
ab = a + b
ab.result()
ab = a - b
ab.result()
ab = a * b
ab.result()
ab = a / b
ab.result()

