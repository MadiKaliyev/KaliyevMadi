# Задания №3
# Напишите программу с пустым классом Country. Опишите наследуемые от класса
# Country классы Russia, Canada, Germany. Добавьте каждому классу поле population и опишите
# метод setPopulation и getPopulation.

class Country:
    pass

class Russia(Country):
    def __init__(self):
        self.population = ''

    def setPopulation(self, population):
        self.population = population

    def getPopulation(self):
        return self.population

class Canada(Country):
    def __init__(self):
        self.population = ''

    def setPopulation(self, population):
        self.population = population

    def getPopulation(self):
        return self.population

class Germany(Country):
    def __init__(self):
        self.population = ''

    def setPopulation(self, population):
        self.population = population

    def getPopulation(self):
        return self.population

russia = Russia()
russia.setPopulation(140000000)
print(russia.getPopulation())

canada = Canada()
canada.setPopulation(38000000)
print(canada.getPopulation())

germany = Germany()
germany.setPopulation(83000000)
print(germany.getPopulation())
