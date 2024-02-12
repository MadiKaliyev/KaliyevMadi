# Задание №1
# а) Сделать набросок дизайна программы в figma / paint для программы, которая читает
# все excel-файлы в папке и выводит на экран общее количество строк.
# б) Разработать эту программу на библиотеке tkinter.

from tkinter import *
from tkinter import filedialog as load
import openpyxl

def download():
    file = load.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file:
            book = openpyxl.load_workbook(file)
            sheet = book.active
            rows = sheet.max_row
            result_text.config(state=NORMAL)
            result_text.insert(END, f"Число строк в файле {rows}")

window = Tk()
window.title("Excel")

label = Label(window, text='Загрузка файла Excel', font=("Trajan Pro", 20), bg='yellow')
label.grid(column=3, row=2)
window.geometry('300x130')

button = Button(window, text='Обзор', command=download)
button.grid(column=3, row=5)

result_text = Text(window, height=2, width=25)
result_text.grid(column=3, row=7)

window.mainloop()
