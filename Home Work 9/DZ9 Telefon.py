# Задание №3.
# Напишите программу, в которой я ввожу телефонный номер. Необходимо проверить
# правильность формата телефонного номера.
import re
def telefon(x):
    pattern = r"^(?:\+?7|8)?(?:\s*|-*)?\(?\d{3}\)?(?:\s*|-*)?\d{3}(?:\s*|-*)?\d{2}(?:\s*|-*)?\d{2}$"
    if re.match(pattern,x):
        return True
    else:
        False


a = input("Введите текст: ")
if telefon(a):
    print("формат верный ")
else:
    print("Формат не верный")