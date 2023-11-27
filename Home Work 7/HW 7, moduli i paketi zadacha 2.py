# Задание №2.
# Напишите программу, создайте случайный вектор размера 30 и найдите среднее
# значение.
import random
a = [random.randint(0,29)for i in range (30)]
srednee = sum(a)/len(a)
print(f"Список случайных чисел: {a}\nСредняя сумма:{int(srednee)}")