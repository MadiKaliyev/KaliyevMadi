# Задание №1
# Дан текстовый файл. Необходимо создать новый файл, в который требуется переписать
# из исходного файла все слова, состоящие не менее чем из семи букв.
import fileinput
import sys

with open("ishodii.txt", 'r', encoding='utf-8') as a:
    text = a.read()
    words = text.split()
    print(words)
    print()

with open("vtorichnii.txt", 'w', encoding='utf-8') as a_new:
    for i in words:
        if len(i) >= 7:
            a_new.write(i + '\n')
            print(i,end=" ")