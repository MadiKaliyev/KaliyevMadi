# Задания №2
# Написать программу, в которой есть главный класс Games со статическим полем Year,
# опишите конструктор присваивающий значение полю Year, также опишите метод getName,
# который возвращает имя игры. На основе главного класса путем наследования опишите
# четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу
# дополнительные поля и переопределите у всех классов метод getName.

class Games:
    Year = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def getName(self):
        return self.name

class PCGames(Games):
    def __init__(self, name, year, platforma):
        super().__init__(name, year)
        self.platforma = platforma

    def getName(self):
        return self.name, 'PC'

class PS4Games(Games):
    def __init__(self, name, year, populyarnost):
        super().__init__(name, year)
        self.populyarnost = populyarnost

    def getName(self):
        return self.name, 'Приставка'

class XboxGames(Games):
    def __init__(self,name, year, otlichee):
        super().__init__(name, year)
        self.otlichee = otlichee

    def getName(self):
        return self.name, 'Тоже приставка'

class MobileGames(Games):
    def __init__(self, name, year,priemuchestvo):
        super().__init__(name, year)
        self.priemuchestvo = priemuchestvo

    def getName(self):
        return self.name, 'Royal Match'


PC_Games = PCGames('CS2',2023,'Steam')
PS4_Games = PS4Games('maincraft', 2011, 'Приставка к телевизору')
Xbox_Games = XboxGames('Halo Infinite', 2021, 'Таже приставка только с другим именем')
Mobile_Games = MobileGames("Among Us", 2018, "iOS, Android")

print(PC_Games.getName(), PS4_Games.getName(), Xbox_Games.getName(), Mobile_Games.getName())