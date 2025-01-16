# Задания №2
# Пересмотрите алгоритм решения прошлой практической работы, с использованием
# инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
# Написать программу, в которой есть главный класс Games со статическим полем Year,
# опишите конструктор присваивающий значение полю Year, также опишите метод getName,
# который возвращает имя игры. На основе главного класса путем наследования опишите
# четыре класса PCGames, PS4Games, XboxGames, MobileGames. Добавьте каждому классу
# дополнительные поля и переопределите у всех классов метод getName.

class Games:
    Year = 0

    def __init__(self, year):
        self.__class__.Year = year

    def getName(self):
        pass

class PCGames(Games):
    def __init__(self, year, name):
        super().__init__(year)
        self.neme = name

    def getName(self):
        return self.neme

class PS4Games(Games):
    def __init__(self, year, name):
        super().__init__(year)
        self.name = name

    def getName(self):
        return self.name

class XboxGames(Games):
    def __init__(self, year, name):
        super().__init__(year)
        self.name = name

    def getName(self):
        return self.name

class MobileGames(Games):
    def __init__(self, year, name):
        super().__init__(year)
        self.name = name

    def getName(self):
        return self.name

pc_game = PCGames(2023, "Cyberpunk 2077")
ps4_game = PS4Games(2020, "The Last of Us Part II")
xbox_game = XboxGames(2021, "Halo Infinite")
mobile_game = MobileGames(2019, "Among Us")

print(pc_game.getName())
print(ps4_game.getName())
print(xbox_game.getName())
print(mobile_game.getName())