# # 2. Дан список чисел (содержащий не менее двух элементов). Найдите в нем два
# # ближайших друг к другу числа (то есть два числа с наименьшей разностью).
# # Выведите эти числа в порядке не убывания.
# # Используйте встроенную сортировку языка Python. Решение должно иметь сложность
# встроенной сортировки + O(n).

def blizhnie_chisla(x):
    x.sort()
    max_zhnach = x[-1]
    for i in range(len(x)-1):
        sravnenie = x[i+1]-x[i]
        if sravnenie < max_zhnach:
            max_zhnach = sravnenie
            blizhnii = x[i], x[i+1]
    return blizhnii


a = list(map(int,input("Введите числа через пробел: ").split()))
c = blizhnie_chisla(a)
print(f"Отсортированный список не по убыванию: {a}")
print(f"Ближайшие друг к другу числа: {c[0]} и {c[1]}")

