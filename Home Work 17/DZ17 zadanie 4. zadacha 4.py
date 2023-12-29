# Задание № 4
# Создайте класс «Дробь». Необходимо хранить в полях класса: числитель и знаменатель.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса. Также создайте методы класса для выполнения арифметических
# операций (сложение, вычитание, умножение, деление)

class Drob:
    def __init__(self):
        self.chislitel = ''
        self.znamenatel = ''

    def vvod(self):
        self.chislitel = int(input('Введите числитель: '))
        self.znamenatel = int(input('Введите знаменатель: '))


    def vivod(self):
        print('Числитель:',self.chislitel)
        print('Знаменатель:', self.znamenatel)

    ravno = '='
    def a(self):
        return self.chislitel
    def b(self):
        return self.znamenatel
    def slozhenie(self):
        resultat = self.znamenatel + self.chislitel
        return str(self.znamenatel) + ' + ' + str(self.chislitel) + ' = ' + str(resultat)
    def vichitanie(self):
        if self.chislitel > self.znamenatel:
            resultat = self.chislitel - self.znamenatel
            return str(self.chislitel) + ' - ' + str(self.znamenatel) + ' = ' + str(resultat)
        else:
            resultat = self.znamenatel - self.chislitel
            return str(self.znamenatel) + ' - ' + str(self.chislitel) + ' = ' + str(resultat)
    def delenie(self):
        if self.chislitel > self.znamenatel:
            resultat = self.chislitel / self.znamenatel
            return str(self.chislitel) + ' / ' + str(self.znamenatel) + ' = ' + str(resultat)
        else:
            resultat = self.znamenatel / self.chislitel
            return str(self.znamenatel) + ' / ' + str(self.chislitel) + ' = ' + str(resultat)
    def umnozhenie(self):
        resultat = self.znamenatel * self.chislitel
        return str(self.znamenatel) + ' * ' + str(self.chislitel) + ' = ' + str(resultat)
try:
    ravno = '='
    Drobi = Drob()
    Drobi.vvod()
    print('')
    Drobi.vivod()
    print('')
    print('***', Drobi.a())
    print('***', Drobi.b())
    print('')
    print(Drobi.slozhenie())
    print(Drobi.vichitanie())
    print(Drobi.delenie())
    print(Drobi.umnozhenie())

except ValueError:
    print('Введите целые числа: ')
except ZeroDivisionError:
    print('На ноль нельзя делить')
