# Выполните следующее задание:
# Создайте класс Roman (РимскоеЧисло), представляющий римское число и
# поддерживающий операции +, -, *, /.
# При реализации класса:
# операции +, -, *, / реализуйте как специальные методы
# методы преобразования как статические методы
class Roman:
    roman_numerals = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
        'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    def __init__(self, roman_numeral):
        self.value = self.to_decimal(roman_numeral)

    @staticmethod
    def to_decimal(roman_numeral):
        decimal_value = 0
        prev_value = 0
        for numeral in reversed(roman_numeral):
            current_value = Roman.roman_numerals[numeral]
            if current_value >= prev_value:
                decimal_value += current_value
            else:
                decimal_value -= current_value
            prev_value = current_value
        return decimal_value

    @staticmethod
    def to_roman(decimal_value):
        result = ''
        for numeral, value in sorted(Roman.roman_numerals.items(), reverse=True, key=lambda x: x[1]):
            while decimal_value >= value:
                result += numeral
                decimal_value -= value
        return result

    def __add__(self, other):
        if isinstance(other, Roman):
            result = self.value + other.value
            return Roman(Roman.to_roman(result))
        else:
            raise ValueError("Cannot add Roman numeral with non-Roman numeral")

    def __sub__(self, other):
        if isinstance(other, Roman):
            result = self.value - other.value
            return Roman(Roman.to_roman(result))
        else:
            raise ValueError("Cannot subtract Roman numeral with non-Roman numeral")

    def __mul__(self, other):
        if isinstance(other, Roman):
            result = self.value * other.value
            return Roman(Roman.to_roman(result))
        else:
            raise ValueError("Cannot multiply Roman numeral with non-Roman numeral")

    def __truediv__(self, other):
        if isinstance(other, Roman):
            result = self.value // other.value
            return Roman(Roman.to_roman(result))
        else:
            raise ValueError("Cannot divide Roman numeral with non-Roman numeral")

    def __str__(self):
        return Roman.to_roman(self.value)

num1 = Roman('XII')
num2 = Roman('III')

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
