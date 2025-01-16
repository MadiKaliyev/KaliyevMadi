# Задания №1
# Создайте класс Число (или используйте уже ранее созданный вами). Класс число хранит
# внутри одно значение. Используя перегрузку операторов реализуйте для него
# арифметические операции для работы с числом (операции +, -, *, /).

class Chislo:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Chislo(self.x + other.x)

    def __sub__(self, other):
        if self.x > other.x:
            return Chislo(self.x - other.x)
        else:
            return Chislo(other.x - self.x)

    def __mul__(self, other):
        return Chislo(self.x * other.x)

    def __truediv__(self, other):
        if self.x > other.x :
            return Chislo(self.x / other.x)
        else:
            return Chislo(other.x / self.x)

    def result(self):
        print(self.x)

a = Chislo(6)
b = Chislo(7)
c = a + b
c.result()
c = a - b
c.result()
c = a * b
c.result()
c = a / b
c.result()