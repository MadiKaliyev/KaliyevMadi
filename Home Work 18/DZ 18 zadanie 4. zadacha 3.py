# Задания №3
# Пересмотрите алгоритм решения прошлой практической работы, с использованием
# инкапсуляции. Реализуйте старый алгоритм с использованием полиморфизма.
# Напишите программу с пустым классом Country. Опишите наследуемые от класса
# Country классы Russia, Canada, Germany. Добавьте каждому классу поле population и опишите
# метод setPopulation и getPopulation.


class Country:
    pass

class Russia(Country):
    def __init__(self, population):
        self.population = population

    def setPopulation(self):
        return self.population

    def getPopulation(self):
        return self.population

class Canada(Country):
    def __init__(self, population):
        self.population = population

    def setPopulation(self):
        return self.population

    def getPopulation(self):
        return self.population

class Germany(Country):
    def __init__(self, population):
        self.population = population

    def setPopulation(self):
        return self.population

    def getPopulation(self):
        return self.population



russia = Russia(input("Введите популяцию для России: "))
canada = Canada(input("Введите популяцию для Канады: "))
germany = Germany(input("Введите популяцию для Германии: "))
print(russia.getPopulation())
print(canada.getPopulation())
print(germany.getPopulation())