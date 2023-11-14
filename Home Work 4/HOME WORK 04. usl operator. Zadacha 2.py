# Задание №2.
# Напишите программу обмена валют, где я ввожу сумму в тенге и выбираю на какую
# валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8).
usd = 420
eur = 510
rub = 5.8
currency = int(input("Введите сумму в тенге: "))
if currency <= 0:
    print("Введите положительное число: ")
else:
    currency1 = int(input("[1] USD\n[2] EUR \n[3] RUB" f"\nВыберите валюту: "))
    if currency1 == 1:
        print("Ваша сумма в тенге равна:", currency/usd, "USD")
    elif currency1 == 2:
        print("Ваша сумма в тенге равна:", currency/eur, "EUR")
    elif currency1 == 3:
        print("Ваша сумма в тенге равна:", currency/rub, "RUB")
    else:
        print("Выберите одно из трех: ")


