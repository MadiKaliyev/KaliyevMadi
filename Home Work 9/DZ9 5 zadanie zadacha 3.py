# Задание №1.
# Напишите программу, в которой возвращаются домены из списка e-mail адресов.
import re

def domen(emails):
    domeni = []
    for email in emails:
        username, domain = email.split('@')
        domeni.append(domain)
    return domeni


email_adres = ['1910797@mail.ru','3520456@mail.ru','kaliev-madi@mail.ru']

result = domen(email_adres)
print(result)
