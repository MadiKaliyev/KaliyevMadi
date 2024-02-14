import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog

class JsonRequestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.data_text_edit = QTextEdit(self)
        self.data_text_edit.setReadOnly(True)

        self.fetch_button = QPushButton("Запрос JSON", self)
        self.fetch_button.clicked.connect(self.fetch_json_data)

        self.save_button = QPushButton("Сохранить в файл", self)
        self.save_button.clicked.connect(self.save_to_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.fetch_button)
        layout.addWidget(self.data_text_edit)
        layout.addWidget(self.save_button)

        self.api_url = "https://jsonplaceholder.typicode.com/posts"

    def fetch_json_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            data = response.json()
            formatted_data = "\n".join([f"{item['id']}: {item['title']}" for item in data])
            self.data_text_edit.clear()
            self.data_text_edit.insertPlainText(formatted_data)
        else:
            self.data_text_edit.clear()
            self.data_text_edit.insertPlainText(f"Ошибка при запросе: {response.status_code}")

    def save_to_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)")
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.data_text_edit.toPlainText())
                print(f"Данные успешно сохранены в файл: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    json_app = JsonRequestApp()
    json_app.show()
    sys.exit(app.exec())
