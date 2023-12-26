# Задание №2
# Римское число
# Создайте класс Roman (РимскоеЧисло), представляющий римское число и
# поддерживающий операции +, -, *, /.
# 3
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы
# методы преобразования как статические методы.
# Опишите все исключения, возможные в программе. (Например, неверный вод, ошибка
# деления на 0).

class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            0: '0', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
            20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
            60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 1000: 'M',
            2000: 'MM', 3000: 'MMM', 4000: 'MMMM', 5000: 'MMMMM', 6000: 'MMMMMM',
            7000: 'MMMMMMM', 8000: 'MMMMMMMM', 9000: 'MMMMMMMMM', 10000: 'MMMMMMMMMM'
            }

    def to_roman(self, number):
        if number in self.roman_numerals:
            return self.roman_numerals[number]
        else:
            blizhnii = max(key for key in self.roman_numerals if key <= number)
            remainder = number - blizhnii
            return self.roman_numerals[blizhnii] + self.to_roman(remainder)


class Calculator:
    def __init__(self):
        self.converter = RomanConverter()

    def add(self, a, b):
        roman_a = self.converter.to_roman(a)
        roman_b = self.converter.to_roman(b)

        result = a + b
        result1 = a * b
        result2 = max(a, b) / min(a, b)
        result3 = max(a, b) - min(a, b)

        roman_result = self.converter.to_roman(result)
        roman_result1 = self.converter.to_roman(result1)
        roman_result2 = self.converter.to_roman(int(result2))
        roman_result3 = self.converter.to_roman(int(result3))

        print(f'{roman_a} + {roman_b} = {roman_result}')
        print(f'{roman_a} * {roman_b} = {roman_result1}')
        print(f'{roman_a} / {roman_b} = {roman_result2}')
        print(f'{roman_a} - {roman_b} = {roman_result3}')

try:
    calc = Calculator()


    a = int(input("Введите первое значение: "))
    b = int(input("Введите второе значение: "))

    calc.add(a, b)

except ValueError:
    print("Введите числа: ")
except ZeroDivisionError:
    print("Нельзя делить на ноль: ")

