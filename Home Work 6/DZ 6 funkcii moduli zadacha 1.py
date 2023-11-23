# Задание №1.
# Напишите программу для создания списка, длина которого равна N. После создания
# списка нужно подсчитать нечетные и четные числа. Если нечетных чисел больше, чем четных,
# вывод должен быть «Нет», в остальных ключах «Да».

def chetnechet(numbers):
    nechet = []
    chet = []
    for i in numbers:
        if i % 2 != 0:
            nechet.append(i)
        else:
            chet.append(i)

    return nechet, chet

n = int(input("Введите длину списка: "))
a = []
for i in range(n):
    b = int(input("Введите число: \n"))
    a.append(b)

chet, nechet = chetnechet(a)

if len(chet) > len(nechet):
    print(*chet)
    print(*nechet)
    print("НЕТ")
else:
    print(*nechet)
    print(*chet)
    print("ДА")


