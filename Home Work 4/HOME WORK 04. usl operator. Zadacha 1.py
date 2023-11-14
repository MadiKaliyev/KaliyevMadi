# Задание №1.
# Напишите программу, где я ввожу логин и пароль.
# И если данные были введены верно,
# то мы выводим Authentication completed, иначе Invalid login or password.
# (Логин должен быть user, пароль - qwerty
login = "user"
password = "qwerty"
user1 = str(input("Введите логин: "))
password1 = str(input("Введите пароль: "))
if user1 == login and password1 == password:
    print("Authentication completed")
else:
    print("Invalid login or password")
