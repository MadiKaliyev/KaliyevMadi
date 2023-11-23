# Задание №1.
# Напишите программу для создания списка, длина которого равна N. После создания
# списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
# вывод должен быть «Нет», в остальных ключах «Да».

# def chetnechet(n):
#     c = 0
#     for i in range(n):
#         if i % 2 ==0:
#             return c + 1
#
# n = int(input("Введите длинну списка: " ))
# dlinna = []
# for i in range(n):
#     i += 1
#     a = int(input(f"Введите числа для списка {i} - {n}: "))
# print(dlinna=chetnechet(n))
#
def count_even_odd(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    return "Нет" if odd_count > even_count else "Да"

# Ввод длины списка
N = int(input("Введите длину списка: "))

# Создание списка
my_list = []
for i in range(N):
    num = int(input(f"Введите число {i+1}/{N}: "))
    my_list.append(num)

# Подсчет четных и нечетных чисел
result = count_even_odd(my_list)

# Вывод результата
print(f"Больше ли нечетных чисел, чем четных? {result}")
