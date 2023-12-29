# Задание №1
# Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
# год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Auto:
    def __init__(self):
        self.__name = ''
        self.year = ''
        self.__made = ''
        self.v = ''
        self.color = ''
        self.price = ''

    def vvod(self):
        self.__name = input('Введите название машины: ')
        self.year = input('Введите год выпуска: ')
        self.__made = input('Введите страну изготовителя: ')
        self._v = input('Введите объем двигателя машины: ')
        self.color = input('Введите цвет машины: ')
        self.price = input('Введите цену машины: ')

    def set_name(self, name):
            self.__name = name

    def get_name(self):
            return self.__name

    def year(self):
        return self.year()

    def set_made(self, made):
            self.__made = made

    def get_made(self):
            return self.__made

    def v(self):
        return self._v()

    def color(self):
        return self.color()

    def price(self):
        return self.price()


    def vivod(self):
        print(self.__name)
        print(self.year)
        print(self.__made)
        print(self._v)
        print(self.color)
        print(self.price)

CAR = Auto()
CAR.vvod()
CAR.vivod()
CAR.set_made(made='KZ')
print(CAR.get_made())
