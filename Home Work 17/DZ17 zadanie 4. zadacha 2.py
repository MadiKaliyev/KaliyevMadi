# Задание № 2
# Создайте класс «Город». Необходимо хранить в полях класса: название города, название
# региона, название страны, количество жителей в городе, почтовый индекс города,
# телефонный код города. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

class City:
    def __init__(self):
        self.gorod = ''
        self.region = ''
        self.strana = ''
        self.kolichestvo_zhitelei = ''
        self.index_goroda = ''
        self.tel_kod = ''

    def vvod(self):
        self.gorod = input('Введите город: ')
        self.region = input('Введите регион: ')
        self.strana = input('Введите страну: ')
        self.kolichestvo_zhitelei = input('Введите количество жителей: ')
        self.tel_kod = input('Введите телефонный код города: ')

    def vivod(self):
        print('город:',self.gorod)
        print('регио:', self.gorod)
        print('страна:', self.gorod)
        print('численность людей:', self.gorod)
        print('телефонный код города:', self.gorod)

    def a(self):
        return self.gorod
    def b(self):
        return self.region

    def c(self):
        return self.strana

    def d(self):
        return self.kolichestvo_zhitelei

    def e(self):
        return self.tel_kod


Dannie_goroda = City()

Dannie_goroda.vvod()
print('')
Dannie_goroda.vivod()
print('')
print('***', Dannie_goroda.a())
print('***', Dannie_goroda.b())
print('***', Dannie_goroda.c())
print('***', Dannie_goroda.d())
print('***', Dannie_goroda.e())



