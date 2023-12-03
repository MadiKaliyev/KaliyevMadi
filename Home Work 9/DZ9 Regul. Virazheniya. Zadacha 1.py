# Регулярные выражения
# Задание №1.
# Напишите программу, в которой необходимо вывести первое слово из строки.

import re
def pervoe_slovo(text):
    pattern = r"\b\w+\b"
    pervoe_slovo = re.search(pattern, text)
    return pervoe_slovo.group() if pervoe_slovo else None

a = input("Введите ваше предложение: ")
first = pervoe_slovo(a)
if first:
    print("Первое слово:", first)
else:
    print("В строке нет слов.")

# Ну как вариант. Вдроде тоже выводит )))) хотя могу ошибаться
# a = input(" Введтите текст: ").split()
# print(a[0])



