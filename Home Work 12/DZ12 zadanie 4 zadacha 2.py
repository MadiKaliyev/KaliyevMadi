# Задание №2
# Дан текстовый файл. Необходимо переписать его строки в другой файл. Порядок строк
# во втором файле должен совпадать с порядком строк в заданном файле.

import fileinput
import sys

with open("ishodii.txt", 'r', encoding='utf-8') as a:
    text = a.read()
    print(text)
    print()

with open("vtorichnii.txt", 'w', encoding='utf-8') as a_new:
    for i in text:
        a_new.write(i)
        print(i, end="")