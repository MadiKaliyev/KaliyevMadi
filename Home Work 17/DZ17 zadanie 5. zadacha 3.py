# Задание №3
# Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона,
# дату открытия, страну, город, вместимость. Реализуйте методы класса для ввода данных,
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Stadion:
    def __init__(self):
        self.name = ''
        self.date = ''
        self.country = ''
        self.city = ''
        self.vmestimost = ''

    def vvod(self):
        self.name = input('Введите название: ')
        self.date = input('Введите год выпуска: ')
        self.country = input('Введите издателя: ')
        self.city = input('Ведите жанр: ')
        self.vmestimost = input('Введите автора: ')

    def vivod(self):
        print(self.name)
        print(self.date)
        print(self.country)
        print(self.city)
        print(self.vmestimost)

    def name_zamena(self):
        return self.name

    def date_zamena(self):
        return self.date

    def country_zamena(self):
        return self.country

    def city_zamena(self):
        return self.city

    def vmestimost_zamena(self):
        return self.vmestimost

stadion = Stadion()
stadion.vvod()
print('')
stadion.vivod()
print('')
print(stadion.name_zamena())
print(stadion.date_zamena())
print(stadion.country_zamena())
print(stadion.city_zamena())
print(stadion.vmestimost_zamena())
