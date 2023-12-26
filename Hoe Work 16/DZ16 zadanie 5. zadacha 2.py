# Выполните следующие задание:
# Функция plus_two() выполняет одну простую задачу — выводит результат сложения
# переданного в нее числа 2 и значения переменной number. В переменную number должно быть
# передано число. Обработайте ситуацию, если в эту переменную переданы данные какого-то
# другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных
# — число!».
# Запустите код и проверьте работу кода в консоли.
# Подсказка:
# Используйте конструкцию try/except.В процессе поиска решения попробуйте вывести в
# консоль сумму строки и числа, изучите сообщение об ошибке.В Python есть специальное
# исключение для ситуации, если тип переданного значения не соответствует ожиданиям

def plus_two(x):
    try:
        a = 2 + int(x)
        print(a)
    except TypeError:
        print('Ожидаемый тип данных— число!')
    except ValueError:
        print("Ожидаемый тип данных— число!")
    except ZeroDivisionError:
        print("На ноль делить нельзя")

chislo = input("Введите число: ")
plus_two(chislo)
