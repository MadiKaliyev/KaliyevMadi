# Задание №2
# В текущей папке лежит две других папки: vasya и mila, причём в этих папках могут
# лежать файлы с одинаковыми именами, например vasya/kursovaya.doc и mila/kursovaya.doc.
# Скопируйте все файлы из этих папок в текущую папку назвав их следующим образом:
# vasya_kursovaya.doc, mila_test.pdf.
import fileinput
import sys
import os
import shutil


Madi = 'C:/Users/Madi/Desktop/DZ12/Madi/'
Assel = 'C:/Users/Madi/Desktop/DZ12/Assel/'

shutil.copyfile(Madi + 'kursovaya.docx', 'C:/Users/Madi/Desktop/DZ12/Madi.docx')
shutil.copyfile(Assel + 'kursovaya.docx', 'C:/Users/Madi/Desktop/DZ12/Assel.pdf')
