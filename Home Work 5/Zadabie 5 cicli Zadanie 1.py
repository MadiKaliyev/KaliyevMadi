# Циклы
# Задание №1.
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка
# потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
n = int(input("Введите число n: "))
a = 0 
for i in range(1, n + 1):
    a += i
for j in range(n - 1):
    a -= int(input("Введите известные карточки: "))
print(f"Отсутствует: {a}")