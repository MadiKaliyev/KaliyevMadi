# Используя механизм множественного наследования разработайте класс “Автомобиль”.
# Должны быть классы «Колеса», «Двигатель», «Двери».

class Kolesa:
    def __init__(self, deistvie):
        self.deistvie = deistvie

    def vrachenie(self):
        return 'Крутятся'

class Dvigatel:
    def __init__(self, deistvie1):
        self.deistvie1 = deistvie1

    def rabota(self):
        return 'Работа двигателя'

class Dveri:
    def __init__(self, deistvie2):
        self.deistvie2 = deistvie2

    def otkrivanie(self):
        return 'Открывание'


class Automobile(Kolesa, Dvigatel, Dveri):
    def __init__(self, deistvie, deistvie1, deistvie2):
        super().__init__(deistvie)
        super().__init__(deistvie1)
        super().__init__(deistvie2)

    def upravlenie(self):
        return 'Движение автомобиля!'

my_auto = Automobile(4, '520 HP', 5)
print(my_auto.upravlenie())
print(my_auto.vrachenie())
print(my_auto.rabota())
print(my_auto.otkrivanie())
