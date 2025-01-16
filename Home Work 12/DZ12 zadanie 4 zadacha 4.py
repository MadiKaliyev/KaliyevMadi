# Задание №4
# Дан текстовый файл. Добавить в него строку из двенадцати звездочек (************),
# поместив ее после последней из строк, в которых нет запятой. Если таких строк нет, то новая
# строка должна быть добавлена после всех строк имеющегося файла. Результат записать в
# другой файл.
import fileinput
import sys

with open("ishodii.txt", 'r', encoding='utf-8') as a:
    text = a.readlines()

a1 = 0
for x, x1 in enumerate(text):
    if ',' not in x1:
        a1 = x
if a1 == -1:
    text.append('************\n')
else:
    text.insert(a1 + 1, '************\n')

with open("vtorichnii.txt", 'w', encoding='utf-8') as a_new:
        a_new.writelines(text)
