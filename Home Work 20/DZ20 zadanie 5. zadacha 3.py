# Задание №3
# Вам необходимо создать класс Airplane (самолет).
# С помощью перегрузки операторов реализовать:
# Проверка на равенство типов самолетов (операция = =);
# Увеличение и уменьшение пассажиров в салоне самолета (операции + - += -=);
# Сравнение двух самолетов по максимально возможному количеству пассажиров на
# борту (операции > < <= >=)

class Airplane:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Airplane):
            return Airplane(self.x + other.x, self.y + other.y)
        else:
            return Airplane(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Airplane):
            return Airplane(self.x - other.x, self.y - other.y)
        else:
            return Airplane(self.x - other, self.y - other)

    def __iadd__(self, other):
            self.x += other
            self.y += other
            return self

    def __isub__(self, other):
        self.x -= other
        self.y -= other
        return self

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        return self.x < other.x

    def __ge__(self, other):
        return self.x >= other.x

    def __le__(self, other):
        return self.x <= other.x


air1 = Airplane(733, 150)
air2 = Airplane(747, 200)

print(air1 == air2)
print(air1 < air2)
print(air1 > air2)
air3 = air1 + air2
air4 = air1 - air2
print(air3.y)
print(abs(air4.y))
print((air1 + 2).y)
print((air1 - 3).y)
print((air2 + 2).y)
print((air2 - 3).y)

