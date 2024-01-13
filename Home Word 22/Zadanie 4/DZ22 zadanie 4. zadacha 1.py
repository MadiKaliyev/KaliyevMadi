# Задание №1
# а) Напишите скрипт, который будет создавать виртуальное окружение и устанавливать
# туда библиотеку openpyxl.
# б) Напишите пример приложения-калькулятор на input.
# в) Соберите это приложение в исполняемый файл («.exe»).

import subprocess
import sys
import openpyxl
import subprocess
import sys
import os

def setup_virtualenv():
    try:
        subprocess.check_call([sys.executable, '-m', 'venv', 'myenv'])
        print("Виртуальное окружение создано.")

        activate_script = os.path.join('myenv', 'Scripts', 'activate')

        subprocess.check_call([activate_script], shell=True)

        subprocess.check_call(['pip', 'install', 'openpyxl'])
        print("Библиотека openpyxl установлена.")

    except subprocess.CalledProcessError as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    setup_virtualenv()

import math
def fibo(x):
    if x < 2:
        return x
    else:
        return fibo(x-1) + fibo(x - 2)

while True:
    a = int(input("Какое действие желаете провести: \n1 умножение \n2 деление \n3 плюс \n4 минус \n5 возведение в степень \n6 нахождение факториала \n7 число фиббоначи \n8 тригонометрических функций\n"))
    if a < 1 or a > 8:
        print("Выберите из списка: ")
    elif a == 1:
        a1 = float(input("Введите первое число: "))
        b1 = float(input("Введите второе число: "))
        print((lambda x1, x2: x1 * x2)(a1, b1))
    elif a == 2:
        a1 = float(input("Введите первое число: "))
        b1 = float(input("Введите второе число: "))
        print((lambda x1, x2: x1 / x2)(a1, b1))
    elif a == 3:
        a1 = float(input("Введите первое число: "))
        b1 = float(input("Введите второе число: "))
        print((lambda x1, x2: x1 + x2)(a1, b1))
    elif a == 4:
        a1 = float(input("Введите первое число: "))
        b1 = float(input("Введите второе число: "))
        print((lambda x1, x2: x1 - x2)(a1, b1))
    elif a == 5:
        a1 = int(input("Введите число: "))
        b1 = float(input("Введите степень: "))
        print(pow(a1, b1))
    elif a == 6:
        a1 = int(input("Введите число для вычисления факториала: "))
        print(math.factorial(a1))
    elif a == 7:

        a1 = int(input("Введите число Фибоначчи: "))
        c = fibo(a1)
        print(f"Число Фибоначчи от {a1} равно {c}")
    elif a == 8:
        a1 = int(input("Введите угол "))
        print(f"косинус угла {a1} равен {math.cos(a1)}, синус угла {a1} равен {math.sin(a1)}, тангенс угла {a1} равен {math.tan(a1)}, катангенс угла {a1} равен {math.atan(1 / math.tan(a1))}")
    b = int(input("Желаете произвести еще вычисление: ДА [1] НЕТ [2]\n"))
    if b == 1:
        continue
    else:
        break