# Задание №2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год
# выпуска, издателя, жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода
# данных, реализуйте доступ к отдельным полям через методы класса


class BOOK:
    def __init__(self):
        self.name = ''
        self.year = ''
        self.made = ''
        self.zhanr = ''
        self.autor = ''
        self.price = ''

    def vvod(self):
        self.name = input('Введите название: ')
        self.year = input('Введите год выпуска: ')
        self.made = input('Введите издателя: ')
        self.zhanr = input('Ведите жанр: ')
        self.autor = input('Введите автора: ')
        self.price = input('Введите цену: ')

    def vivod(self):
        print(self.name)
        print(self.year)
        print(self.made)
        print(self.zhanr)
        print(self.autor)
        print(self.price)

    def name_zamena(self):
        return self.name

    def year_zamena(self):
        return self.year

    def made_zamena(self):
        return self.made

    def zhanr_zamena(self):
        return self.zhanr

    def autor_zamena(self):
        return self.autor

    def price_zamena(self):
        return self.price

Kniga = BOOK()
Kniga.vvod()
print('')
Kniga.vivod()
print('')
print(Kniga.name_zamena())
print(Kniga.year_zamena())
print(Kniga.made_zamena())
print(Kniga.zhanr_zamena())
print(Kniga.autor_zamena())
print(Kniga.price_zamena())
