# Задание №1
# Создайте класс Device, который содержит информацию об устройстве. С помощью
# механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о
# кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder
# (содержит информацию о мясорубке). Каждый из классов должен содержать необходимые
# для работы методы.

class Device:
    def __init__(self, model, marka):
        self.model = model
        self.marka = marka

    def __str__(self):
        return f'{self.marka}, {self.model}'


class CoffeeMachine(Device):
    def __init__(self, model, marka, type):
        super().__init__(model, marka)
        self.type = type

    def __str__(self):
        return f'{self.marka}, {self.model}, {self.type}'
    def make_coffe(self):
        return self.type

class Blender(Device):
    def __init__(self, model, marka, speed):
        super().__init__(model, marka)
        self.speed = speed

    def __str__(self):
        return f'{self.marka}, {self.model}, {self.speed}'

    def blend(self, item):
        return f'{item}, {self.speed}'

class MeatGrinder(Device):
    def __init__(self, model, marka, meat):
        super().__init__(model, marka)
        self.meat = meat

    def __str__(self):
        return f'{self.marka}, {self.model}, {self.meat}'

    def meater(self, farsh):
        return f'{farsh}, {self.meat}'


coffe_machine = CoffeeMachine('Марка1', 'Модель1', 'Эспрессо')
blender = Blender('Марка2', 'Модель2', 50000)
meatgrinder = MeatGrinder('Марка3','Модель3', 'Мясорубка в хлам')

print(coffe_machine)
print(coffe_machine.make_coffe())
print(blender.speed)
print(blender.blend('Фреш'))
print(meatgrinder)
print(meatgrinder.meater('Мясо'))