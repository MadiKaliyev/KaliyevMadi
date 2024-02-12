# Задание №1
# а) Сделать набросок дизайна программы в figma / paint для программы, которая делает
# запрос на сайт jsonplaceholder с определённым id.
# б) Разработать эту программу на библиотеке tkinter.
# в) Реализовать сохранение полученного объекта в папку.
# В качестве ответа прикрепить скрин и ссылку на github.
import tkinter as tk
from tkinter import ttk
import requests
import json

class Json:
    def __init__(self, root):
        self.root = root
        self.root.title("Json")

        self.label_id = ttk.Label(root, text="Write ID:", font=("Protest Revolution", 20))
        self.label_id.grid(row=0, column=0, padx=5, pady=5)

        self.entry_id = ttk.Entry(root)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        self.button_get_data = ttk.Button(root, text="Получить данные", command=self.get_data)
        self.button_get_data.grid(row=0, column=2, padx=5, pady=5)

        self.text_result = tk.Text(root, height=10, width=50)
        self.text_result.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.button_save = ttk.Button(root, text="Save File", command=self.save_to_file)
        self.button_save.grid(row=2, column=0, columnspan=3, pady=10)

    def get_data(self):
            user_id = int(self.entry_id.get())
            response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
            user_data = response.json()
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, json.dumps(user_data, indent=4))

    def save_to_file(self):
            user_id = int(self.entry_id.get())
            response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
            user_data = response.json()

            with open(f"user_{user_id}_data.json", "w") as file:
                json.dump(user_data, file, indent=4)
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Данные сохранены в файл 'user_{user_id}_data.json'.")


root = tk.Tk()
id = Json(root)
root.mainloop()
