# Задание №2
# Создайте класс Complex (комплексное число).
# Создайте перегруженные операторы для реализации арифметических операций для по
# работе с комплексными числами (операции +, -, *, /).

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __truediv__(self, other):
        delenie = other.x ** 2 + other.y ** 2
        x = (self.x * other.x + self.y * other.y) / delenie
        y = (self.y * other.x - self.x * other.y) / delenie
        return Complex(x, y)

    def __str__(self):
        return f"({self.x}{' + ' if self.y >= 0 else ' - '}{abs(self.y)}i)"


x = Complex(2,3)
y = Complex(-5, -1)
print(x + y)
print(x - y)
print(x * y)
print(x/y)



