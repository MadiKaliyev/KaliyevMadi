# Задание № 1
# Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО, дату рождения,
# контактный телефон, город, страну, домашний адрес. Реализуйте методы класса для ввода
# данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Human:
    def __init__(self):
        self.fio = ''
        self.data = ''
        self.tel = ''
        self.city = ''
        self.country = ''
        self.adres = ''

    def vvod(self):
        self.fio = input('Введите ФИО: ')
        self.data = input('Введите дату рождения: ')
        self.tel = input('Введите ваш номер телефона: ')
        self.city = input('Ведите ваш город: ')
        self.country = input('Введите страну: ')
        self.adres = input('Введите адрес: ')

    def vivod(self):
        print('ФИО:',self.fio)
        print('Дата рождения:', self.data)
        print('Телефон:', self.tel)
        print('Город:', self.city)
        print('Страна:', self.country)
        print('Адрес:', self.adres)

    def fio_zamena(self):
        return self.fio + ' ' + ' ***'
    def data_zamena(self):
        return self.data + ' ' + '---'
    def tel_zamena(self):
        return self.tel + ' ' + '*|*|*|*'
    def city_zamena(self):
        return self.city + ' ' + '%%%%%%'
    def country_zamena(self):
        return self.country + ' ' + '%/%/%/%/'
    def adres_zamena(self):
        return self.adres + ' '+'#####'

Chelovek = Human()
Chelovek.vvod()
print('')
Chelovek.vivod()
print('')
print('ФИО:', Chelovek.data_zamena())
print('Дата рождения:', Chelovek.data_zamena())
print('Телефон', Chelovek.tel_zamena())
print('Город', Chelovek.city_zamena())
print('Страна', Chelovek.country_zamena())
print('Адрес', Chelovek.adres_zamena())


