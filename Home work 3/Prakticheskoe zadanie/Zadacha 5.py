# Задание №5. День недели
# Напишите программу, которая по введенному номеру дня недели
# (понедельник – первый день недели – 1, вторник – второй день недели – 2)
# определяет выходной это или будний день. Например,
a = int(input("Введите день: "))
if a >= 1 and a <= 5:
    print("Рабочий день")
elif a > 5 and a <= 7:
    print("Выходной")
else:
    print("Не верный вариант")