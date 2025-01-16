# Задание №1
# В текущей папке лежат две другие папки: video и sub. Создайте новую папку watch_me
# и переложите туда содержимое указанных папок (сами папки класть не надо).
import os
import fileinput
import sys
import shutil
import os


put = os.getcwd()

video = os.path.join(put, 'video')
sub = os.path.join(put, 'sub')
watch_me = os.path.join(put, 'watch_me')

# Создание папки watch_me, если она не существует
if not os.path.exists(watch_me):
    os.mkdir(watch_me)

# Копирование содержимого папок video и sub в watch_me
for papka in [video, sub]:
    for item in os.listdir(papka):
        item_path = os.path.join(papka, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, watch_me)