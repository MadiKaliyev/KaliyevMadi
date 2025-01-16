# Задание №3
# Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово
# quit. После завершения ввода программа должна объединить содержимое всех перечисленных
# пользователем файлов в один.
import os
import fileinput
import sys
import shutil

def x(x1,x2):
    if x1:
        with open(x2, 'w') as papka_itog:
            for i in x1:
                if os.path.exists(i):
                    with open(i, 'r') as papka1:
                        soderzhimoe1 = papka1.read()
                        papka_itog.write(soderzhimoe1)

                else:
                    print("э нэт такой")
        return x2
    else:
        return 'Нет такой'

nazvaniya = []
while True:
    papki = input("Введите названия папок: ")

    if papki == 'quit':
        break
    nazvaniya.append(papki)

a = x(nazvaniya,'new.txt')
print(a)

