# Выполните следующее задание:
# Пересмотрите алгоритм решения прошлой практической работы, с использованием
# инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
# Напишите программу, в которой есть главный класс с текстовым полем. В главное
# классе должен быть метод для присваивания значения полю: без аргументов и с одним
# текстовым аргументом. Объект главного класса создаётся передачей одного текстового
# аргумента конструктору. На основе главного класса создается класса потомок.
# В классепотомке нужно добавить числовое поле. У конструктора класса-потомка два аргумента

class Main:
    def __init__(self, x):
        self._x = x

    def set_text(self, x=None):
        if x:
            self._x = x
        else:
            self._x = input("Введите текстовое значение: ")

    def get_text(self):
        return self._x


class Potomok(Main):
    def __init__(self, x, x_num):
        super().__init__(x)
        self.x_num = x_num

    def set_number(self, x_num):
        self.x_num = x_num

    def get_number(self):
        return self.x_num


roditel = Main("Hello")
naslednik = Potomok("Hi", 42)

print(roditel.get_text())
print(naslednik.get_text(), naslednik.get_number())


