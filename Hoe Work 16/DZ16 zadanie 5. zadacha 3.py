# Задание №1
# Напишите программу, которая позволяет получить доступ к элементу массива, индекс
# которого выходит за границы, и обработаем соответствующее исключение.

def massiv(chislo, index):
    try:
        a = chislo[index]
        print(f"Значение элемента с индексом {index}: {a}")
    except IndexError:
        print("Ошибка: Индекс выходит за границы массива!")

a = [1,2,3,4,5]

massiv(a,2)
massiv(a,8)