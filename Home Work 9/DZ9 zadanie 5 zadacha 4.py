# Задание №2.
# Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву.
import re

def glasnie(x):
    bukvi = "aeiouAEIOUаяуюоеёэиыАЯУЮОЕЁЭИЫ"
    slova = x.split()
    c = [i for i in slova if i[0] in bukvi]
    return c

a = input("Введите ваш текст: ")
b = glasnie(a)
print("Слова, начинающиеся с гласной буквы:", b)

