# Задание №1
# В текущей папке лежат файлы с расширениями .mp3, .flac и .oga. Создайте папки mp3,
# flac, oga и положите туда все файлы с соответствующими расширениями.

import fileinput
import sys
import os
import shutil

a = os.getcwd()

papka = ['mp3', 'flac', 'oga']
for i in papka:
    papka1 = os.path.join(a, i)
    if not os.path.exists(papka1):
        os.makedirs(papka1)

# Перемещение файлов
for file in os.listdir(a):
    if file.endswith('.mp3'):
        shutil.move(os.path.join(a, file), os.path.join(a, 'mp3', file))
    elif file.endswith('.flac'):
        shutil.move(os.path.join(a, file), os.path.join(a, 'flac', file))
    elif file.endswith('.oga'):
        shutil.move(os.path.join(a, file), os.path.join(a, 'oga', file))
