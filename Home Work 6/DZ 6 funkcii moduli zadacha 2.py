# Задание №2.
# Создайте вложенный список размером 3*3 через функцию. И посчитайте сумму
# элементов главной диагонали.
def spisok():
    stroka = []
    for i in range(3):
        stolbec = []
        for j in range(3):
            element = int(input(f"Введите элемент {i+1}-строка: {j+1}-столбец: "))
            stolbec.append(element)
        stroka.append(stolbec)
    return stroka
def diagonal(stroka):
    diagonal_sum = 0
    for i in range(3):
        diagonal_sum += stroka[i][i]
    return diagonal_sum

stroka = spisok()

print("Сумма по диагонали равна:")
for stilbec in stroka:
    print(*stilbec)

diagonal_sum = diagonal(stroka)
print(f"Сумма элементов главной диагонали: {diagonal_sum}")
