import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

class Excel:
    def __init__(self, master):
        self.master = master
        self.master.title("Open Exel")

        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.label = tk.Label(self.frame, text="Выберите папку:")
        self.label.grid(row=0, column=0, sticky="w", pady=(0, 10))

        self.folder_path = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.folder_path, width=40)
        self.entry.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=(0, 5))

        self.browse_button = tk.Button(self.frame, text="Обзор", command=self.browse_folder)
        self.browse_button.grid(row=1, column=2, pady=(0, 10))

        self.process_button = tk.Button(self.frame, text="Открыть", command=self.process_files)
        self.process_button.grid(row=2, column=0, columnspan=3, pady=(10, 0))

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        self.folder_path.set(folder_selected)

    def process_files(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            return

        excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
        total_rows = 0

        for file in excel_files:
            file_path = os.path.join(folder_path, file)
            try:
                df = pd.read_excel(file_path)
                total_rows += len(df)
            except Exception as e:
                print(f"Error reading {file}: {e}")

        result_message = f"Общее количество строк: {total_rows}"
        tk.messagebox.showinfo("Результат", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = Excel(root)
    root.mainloop()
