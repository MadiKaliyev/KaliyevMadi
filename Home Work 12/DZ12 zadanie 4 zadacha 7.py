# Задание №3
# В текущей папке лежат файлы следующего вида: S01E01.mkv, S01E02.mkv, S02E01.mkv
# и т.п., то есть все файлы начинаются с S01 или S02. Создайте папки S01 и S02 и переложите
# туда соответствующие файлы.
import fileinput
import sys
import os
import shutil

Madi = 'C:/Users/Madi/Desktop/DZ12/'

shutil.copyfile(Madi + '1.mkv', Madi + 'Madi/1.mkv')
shutil.copyfile(Madi + '2.mkv', Madi + 'Assel/2.mkv')