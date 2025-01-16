#Задание №2.
# Напишите программу, в которой я ввожу трехзначное число. Найти сумму,
# произведение его цифр. В случае ввода текста, или деления на 0 выведите сообщение.

a = input("введите трехзначное число: ")
try:
    dlinna = list(map(int, a))
    if len(dlinna) != 3:
        print("Число должно быть трехзначное!")
    else:
        b = sum(int(i) for i in str(a))
        print(b)
except ValueError:
    print(" You can’t divide on zero")
except ZeroDivisionError:
    print(" You can’t divide on zero")
