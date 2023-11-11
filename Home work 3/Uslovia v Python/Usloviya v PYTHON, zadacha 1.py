# Задание №1.
# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
# но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки.
# Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B.
# На вход программе в три строки подаются переменные в следующем порядке: A, B, H.
# Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании,
# т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.
# Это первое не самое тривиальное задание на условное выражение. В случаях, когда разбить исполнение программы на несколько направлений,
# стоит внимательно обдумать все условия, которые нужно использовать. Особое внимание стоит уделить строгости используемых условных операторов.
# Для того, чтобы понимать, какой из них стоит использовать, внимательно прочитайте условие задания.
A = int(input("Введите рекомендуемое количество часов для сна: "))
B = int(input("Введите максимально рекомендуемое количество часов для сна: "))
H = int(input("Введите нынешнее количество часов сна: "))
if A > B or A <= 0 or B <= 0 or H < 0:
    print("Введите корректные данные")
elif H < A:
    print("Недосып")
elif H > B:
    print("Пересып")
else:
    print("Это нормально")