# Задание №1
# Дан текстовый файл. Необходимо создать новый файл убрав из него все неприемлемые
# слова. Список неприемлемых слов находится в другом файле.
#

import os
import fileinput
import sys

with open("запреты.docx", "r", encoding='utf-8') as a:
    zapret = a.read()
with open('заданный текс.docx', 'r', encoding='utf-8') as b:
    text = b.read()
with open('новый.docx', 'w', encoding='utf-8') as c:
    for i in text:
        if i not in zapret:
            c.write(i)
        elif i == ' ':
            c.write(i)