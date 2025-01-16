# Задание №4
# Дан текстовый файл. Удалить из него последнюю строку. Результат записать в другой
# файл.

import os
import fileinput
import sys
import shutil
import os

with open('1.txt', 'r') as file:
    lines = file.readlines()
if lines:
    lines.pop()

with open('новый с удаленкой', 'w') as file:
    file.writelines(lines)
