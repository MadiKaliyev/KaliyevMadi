# Задание №4
# Создать класс Flat (квартира). Реализовать перегруженные операторы:
# Проверка на равенство площадей квартир (операция ==);
# Проверка на неравенство площадей квартир (операция !=);
# Сравнение двух квартир по цене (операции > < <= >=).

class Flat:
    def __init__(self, x, price):
        self.x = x
        self.price = price

    def __eq__(self, other):
        return self.x == other.x

    def __ne__(self, other):
        return self.x != other.x

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

flat1 = Flat(150, 20000000)
flat2 = Flat(200, 25000000)

print(flat1 == flat2)
print(flat1 > flat2)
print(flat1 != flat2)
print(flat1 >= flat2)
print(flat1 <= flat2)