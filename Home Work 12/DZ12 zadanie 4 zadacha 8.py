# Задание №4
# В текущей папке лежат файлы вида 2019-03-08.jpg, 2019-04-01.jpg и т.п. Отсортируйте
# файлы по имени и переименуйте их в 1.jpg, 2.jpg, …, 10.jpg.
import os


a = sorted([i for i in os.listdir() if os.path.isfile(i) and i.lower().endswith('.jpg')])

# Переименовываем файлы в порядке от 1 до 10
for i, j in enumerate(a, start=1):
    new = f"№ {i}.jpg"
    os.rename(j, new)
