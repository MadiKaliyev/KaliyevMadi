# Задание №2
# В текущей папке лежат файлы типа Nina_Stoletova.jpg, Misha_Perelman.jpg и т.п.
# Переименуйте их переставив имя и фамилию местами.
import os
import fileinput
import sys
import shutil
import os

foto = os.listdir()
for i in foto:
    if i.endswith('.jpg'):
        name, familiya = os.path.splitext(i)
        parts = name.split('_')
        if len(parts) == 2:
            new_filename = f"{parts[1]}_{parts[0]}{familiya}"
            os.rename(i, new_filename)
            print(i, new_filename)


