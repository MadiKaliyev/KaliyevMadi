# Задание №2.
# Напишите программу, которая считывает целые числа с консоли по одному числу в
# строке.
# Для каждого введённого числа проверить:
# ➢ если число меньше 10, то пропускаем это число;
# ➢ если число больше 100, то прекращаем считывать числа;
# ➢ в остальных случаях вывести это число обратно на консоль в отдельной строке.
while True:
    a = int(input("Введите целое число: "))
    if a < 10:
        continue
    elif a > 100:
        print("Конец: Число больше 100: ")
        break
    else:
        print(a)

