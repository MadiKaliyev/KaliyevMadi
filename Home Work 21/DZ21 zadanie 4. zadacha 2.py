# Задание №2
# Создайте класс для подсчета площади геометрических фигур. Класс должен
# предоставлять функциональность для подсчета площади треугольника по разным формулам,
# площади прямоугольника, площади квадрата, площади ромба. Методы класса для подсчета
# площади должны быть реализованы с помощью статических методов. Также класс должен
# считать количество подсчетов площади и возвращать это значение с помощью статического
# метода.

class Plochad_vigur:
    __count_calculations = 0

    @staticmethod
    def triangle(base, height):
        Plochad_vigur.__count_calculations += 1
        return 0.5 * base * height

    @staticmethod
    def rectangle(length, width):
        Plochad_vigur.__count_calculations += 1
        return length * width

    @staticmethod
    def square(side):
        Plochad_vigur.__count_calculations += 1
        return side * side

    @staticmethod
    def rhombus(diagonal1, diagonal2):
        Plochad_vigur.__count_calculations += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_count_calculations():
        return Plochad_vigur.__count_calculations

area_triangle = Plochad_vigur.triangle(5, 8)
print(f"Площадь треугольника: {area_triangle}")

area_rectangle = Plochad_vigur.rectangle(4, 10)
print(f"Площадь прямоугольника: {area_rectangle}")

area_square = Plochad_vigur.square(6)
print(f"Площадь квадрата: {area_square}")

area_rhombus = Plochad_vigur.rhombus(6, 8)
print(f"Площадь ромба: {area_rhombus}")

count = Plochad_vigur.get_count_calculations()
print(f"Количество подсчетов площади: {count}")


