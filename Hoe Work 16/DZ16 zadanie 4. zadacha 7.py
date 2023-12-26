# Задание №1
# Создайте собственное исключение, которое будет вызываться в случае, если в функцию
# check_name() передано имя длиннее четырёх символов.

class NameTooLongError(Exception):
    pass

def check_name(name):
    if len(name) > 4:
        raise NameTooLongError("Имя длиннее четырех символов!")


try:
    name = input("Введите имя: ")
    check_name(name)
    print("Имя подходит")
except NameTooLongError as j:
    print(j)


