# Задание № 3
# Создайте класс «Страна». Необходимо хранить в полях класса: название страны,
# название континента, количество жителей в стране, телефонный код страны, название
# столицы, название городов страны. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным полям через методы класса.

class Strana:
    def __init__(self):
        self.strana = ''
        self.kontinent = ''
        self.kolichestvo_zhitelei = ''
        self.tel_kod = ''
        self.stolica = ''
        self.goroda = ''

    def vvod(self):
        self.strana = input('Введите город: ')
        self.kontinent = input('Введите регион: ')
        self.kolichestvo_zhitelei = input('Введите страну: ')
        self.tel_kod = input('Введите количество жителей: ')
        self.stolica = input('Введите телефонный код города: ')
        self.goroda = input('Введите телефонный код города: ')

    def vivod(self):
        print('Страна:',self.strana)
        print('Континент:', self.kontinent)
        print('Количество жителей:', self.kolichestvo_zhitelei)
        print('телефонный код страны:', self.tel_kod)
        print('Столица:', self.stolica)
        print('Города:', self.goroda)

    def a(self):
        return self.strana
    def b(self):
        return self.kontinent

    def c(self):
        return self.kolichestvo_zhitelei

    def d(self):
        return self.stolica

    def e(self):
        return self.goroda

    def f(self):
        return self.tel_kod


Dannie_strani = Strana()

Dannie_strani.vvod()
print('')
Dannie_strani.vivod()
print('')
print('***', Dannie_strani.a())
print('***', Dannie_strani.b())
print('***', Dannie_strani.c())
print('***', Dannie_strani.d())
print('***', Dannie_strani.e())
print('***', Dannie_strani.f())