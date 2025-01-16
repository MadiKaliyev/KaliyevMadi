# Задание №4
# Пользователь с клавиатуры вводит названия файлов, до тех пор, пока он не введет слово
# quit. После завершения ввода программа должна записать в итоговый файл символы, которые
# есть во всех перечисленных файлах (символы должны быть в каждом файле)

import os
import fileinput
import sys
import shutil
import os

def x(x1, x2):
    if x1:
        first_file = x1[0]

        if os.path.exists(first_file):
            with open(first_file, 'r', encoding='utf-8') as first:
                common_chars = set(first.read())

            for i in x1[1:]:
                if os.path.exists(i):
                    with open(i, 'r', encoding='utf-8') as file:
                        current_chars = set(file.read())
                        common_chars = common_chars.intersection(current_chars)
                else:
                    print(f"Файл {i} не существует")

            with open(x2, 'w', encoding='utf-8') as output_file:
                output_file.write(''.join(common_chars))
        else:
            print(f"Файл {first_file} не существует")

        return x2
    else:
        return 'Нет такой'

nazvaniya = []
while True:
    papki = input("Введите названия папок: ")

    if papki == 'quit':
        break
    nazvaniya.append(papki)

a = x(nazvaniya, 'new.txt')
print(a)

