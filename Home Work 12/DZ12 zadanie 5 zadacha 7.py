# Задание №3
# В текущей папке лежит файл list.tsv, в котором с новой строки написаны имена
# некоторых других файлов этой папки. Создайте папку list и переложите в неё данные файлы.
import os
import fileinput
import sys
import shutil
import os

file = 'list.tsv'

if not os.path.exists('list'):
    os.makedirs('list')

with open(file, 'r') as a:
    for i in a:
        filename = i.strip()
        if os.path.exists(filename):
            shutil.move(filename, os.path.join('list', filename))

