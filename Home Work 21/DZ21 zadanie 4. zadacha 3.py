# Задание №3
# Создайте класс для подсчета максимума из четырех аргументов, минимума из четырех
# аргументов, среднеарифметического из четырех аргументов, факториала аргумента.
# Функциональность необходимо реализовать в виде статических методов.

class MathOperations:
    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average_of_four(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

a = 5
b = 10
c = 15
d = 20

max_value = MathOperations.max_of_four(a, b, c, d)
min_value = MathOperations.min_of_four(a, b, c, d)
average = MathOperations.average_of_four(a, b, c, d)
factorial_result = MathOperations.factorial(a)

print(f"Максимум из четырех: {max_value}")
print(f"Минимум из четырех: {min_value}")
print(f"Среднеарифметическое из четырех: {average}")
print(f"Факториал числа {a}: {factorial_result}")
