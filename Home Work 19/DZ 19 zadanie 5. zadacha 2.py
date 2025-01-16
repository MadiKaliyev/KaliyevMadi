# Задание №2
# Создайте класс Ship, который содержит информацию о корабле. С помощью механизма
# наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer
# (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

class Ship:
    def __init__(self, type, name):
        self.type = type
        self.name = name

    def __str__(self):
        return f'{self.type},{self.name}'



class Frigate(Ship):
    def __init__(self, type, name, celi):
        super().__init__(type, name)
        self.celi = celi

    def __str__(self):
        return f'{self.type},{self.celi},{self.name}'

    def lodka(self):
        return self.celi

class Cruiser(Ship):
    def __init__(self, type, name, progulka):
        super().__init__(type, name)
        self.progulka = progulka

    def __str__(self):
        return f'{self.type},{self.progulka},{self.name}'

    def lodka1(self):
        return self.progulka

class Destroyer(Ship):
    def __init__(self, name, type, army):
        super().__init__(type, name)
        self.army = army

    def __str__(self):
        return f'{self.type},{self.army},{self.name}'

    def lodka2(self):
        return self.army


frigate = Frigate('Яхта ','Адмирал ','Парусная прогулка')
cruise = Cruiser('Лайнер','Титаник','Круиз')
destroyer = Destroyer('Ясминец','Линкольн', 'Военный')

print(frigate)
print(frigate.lodka())
print(cruise)
print(cruise.lodka1())
print(destroyer)
print(destroyer.lodka2())
