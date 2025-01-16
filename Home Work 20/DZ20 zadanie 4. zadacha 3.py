# Задания №3
# Создайте класс Библиотека. Класс предназначен для хранения информации о
# библиотеке (название, адрес, количество книг). Реализуйте необходимые для класса методы.
# Используя перегрузку операторов реализуйте для него следующие арифметические операции:
# + добавляет к количеству книг указанное значение;
# - вычитает из количества книг указанное значение;
# += добавляет к количеству книг указанное значение;
#  -= вычитает из количества книг указанное значение; Используя перегрузку
# операторов реализуйте (сравнение по количеству книг):
# <;
# >;
# <=;
# >=;
# ==;
# !=.

class Library:
    def __init__(self, name, address, num_books):
        self.name = name
        self.address = address
        self.num_books = num_books

    def __add__(self, other):
        return Library(self.name, self.address, self.num_books + other)

    def __sub__(self, other):
        return Library(self.name, self.address, self.num_books - other)

    def __iadd__(self, other):
        self.num_books += other
        return self

    def __isub__(self, other):
        self.num_books -= other
        return self

    def __lt__(self, other):
        return self.num_books < other.num_books

    def __gt__(self, other):
        return self.num_books > other.num_books

    def __le__(self, other):
        return self.num_books <= other.num_books

    def __ge__(self, other):
        return self.num_books >= other.num_books

    def __eq__(self, other):
        return self.num_books == other.num_books

    def __ne__(self, other):
        return self.num_books != other.num_books

library1 = Library("Library A", "Address A", 100)
library2 = Library("Library B", "Address B", 150)

print(library1.num_books)

library1 += 50
print(library1.num_books)

library1 -= 20
print(library1.num_books)

print(library1 > library2)
print(library1 < library2)
print(library1 == library2)
print(library1 != library2)
