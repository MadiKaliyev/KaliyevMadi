# Задание № 4.
# Напишите программу кошелек.
# Программа будет иметь несколько функций, основные добавление баланса и
# уменьшение баланса кошелька. В теле основной программы, вызовите эти функции,
# организуя диалог с пользователем. У пользователя может быть более двух валют в кошельке.
# Создание словаря для хранения балансов по валютам
# Задание № 4.
# Напишите программу кошелек.
# Программа будет иметь несколько функций, основные добавление баланса и
# уменьшение баланса кошелька. В теле основной программы, вызовите эти функции,
# организуя диалог с пользователем. У пользователя может быть более двух валют в кошельке.
# Создание словаря для хранения балансов по валютам

balance_usd = 0
balance_eur = 0
balance_gbp = 0
def popolnenie(valuta, summa):
    global balance_eur, balance_usd, balance_gbp
    if valuta == "usd":
        balance_usd += summa
        print(f"Ваш баланс {balance_usd} {valuta}")
    elif valuta == "eur":
        balance_eur += summa
        print(f"Ваш баланс равен {balance_eur} {valuta}")
    elif valuta == "gbp":
        balance_gbp += summa
        print(f"(Ваш балас равен {balance_gbp} {valuta}")

def snyatie(valuta, summa):
    global balance_eur, balance_usd, balance_gbp
    if valuta == "usd":
        if balance_usd < summa:
            print("У вас не достаточно средств!")
        else:
            balance_usd -= summa
            print(f"Ваш баланс равен: {balance_usd} {summa}")
    if valuta == "eur":
        if balance_eur < summa:
            print("У вас не достаточно средств!")
        else:
            balance_eur -= summa
            print(f"Ваш баланс равен: {balance_eur} {summa}")
    if valuta == "gbp":
        if balance_gbp < summa:
            print("У вас не достаточно средств!")
        else:
            balance_gbp -= summa
            print(f"Ваш баланс равен: {balance_gbp} {summa}")

def balance(valuta):
    global balance_eur, balance_usd, balance_gbp
    if valuta == "usd":
        print(f"Остаток вашего счета равен = {balance_usd} {valuta}")
    if valuta == "eur":
        print(f"Остаток вашего счета равен = {balance_eur} {valuta}")
    if valuta == "gbp":
        print(f"Остаток вашего счета равен = {balance_gbp} {valuta}")

while True:
    print("******Кошелек******")
    deistvie = input("Желаете снять или пополнить счет: \n\t\t")
    if deistvie == 'пополнить':
        valuta = input("В какой валюте желаете пополнить? в [USD] или в [EUR] или в [GBP]\n\t\t")
        if valuta == "usd" or valuta == "eur" or valuta == "gbp":
            summa = float(input("Введите сумму\n\t\t"))
            popolnenie(valuta, summa)
        else:
            print("Такого действия нет!")
    if deistvie == "снять":
        valuta = input("В какой валюте желаете снять? в [USD] или в [EUR] или в [GBP]\n\t\t")
        if valuta == "usd" or valuta == "eur" or valuta == "gbp":
            summa = float(input("Введите сумму\n\t\t"))
            snyatie(valuta, summa)
        else:
            print("Такого действия нет!\n")
    proverka = input("Желаете проверить остаток счета?: [да] [нет] ")
    if proverka == "да":
        valuta = input("По какой валюте желаете узнать остаток? в [USD] или в [EUR] или в [GBP]\n\t\t")
        if valuta == "usd" or valuta == "eur" or valuta == "gbp":
            balance(valuta)
        else:
            print("Такого действия нет!")