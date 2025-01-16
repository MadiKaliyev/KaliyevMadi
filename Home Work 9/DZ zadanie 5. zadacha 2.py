# Дан одномерный массив числовых значений, насчитывающий N элементов. Добавить к
# элементам массива такой новый элемент, чтобы сумма элементов с положительными
# значениями стала бы равна модулю суммы элементов с отрицательными значениями.
def chisla(x):
    x1 = []
    x2 = []
    for i in range(len(x)):
        if x[i] < 0:
            x1.append(x[i])
        else:
            x2.append(x[i])
    print(x)
    print(f"{abs(sum(x1))}\n{sum(x2)}")

    if sum(x1) % sum(x2) != 0:
        c = sum(x2) - abs(sum(x1))
        x.append(c)
        print(f"NEED {c}\n{x}")
    else:
        c = sum(x1) - sum(x2)
        x.append(c * -1)
        print(x)

def modul(numbers):
    polozhitelnie = [num for num in numbers if num > 0]
    otricatelnie = [num for num in numbers if num < 0]

    summa_polozhitelnih = sum(polozhitelnie)
    summa_otricatelnih = sum(otricatelnie)

    result = summa_polozhitelnih - (summa_polozhitelnih % summa_otricatelnih)
    print(abs(result))


a = [-3, -2, 1, 2, 3, 4]
b = chisla(a)
c = modul(a)

