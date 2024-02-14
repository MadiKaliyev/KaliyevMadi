from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QFileDialog, QVBoxLayout
from docx import Document
from collections import Counter
import re


class WordApp(QWidget):
    def __init__(self):
        super().__init__()

        self.file_path = None

        self.label_result = QLabel("", self)
        self.text_result = QTextEdit(self)
        self.text_result.setReadOnly(True)

        self.button_get_data = QPushButton("Получить данные", self)
        self.button_get_data.clicked.connect(self.get_and_display_data)

        self.button_load_file = QPushButton("Загрузить файл Word", self)
        self.button_load_file.clicked.connect(self.load_word_file)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button_get_data)
        layout.addWidget(self.button_load_file)
        layout.addWidget(self.text_result)
        layout.addWidget(self.label_result)


    def most_frequent_word(self, docx_file_path):
        doc = Document(docx_file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + " "
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)

        words = text.split()

        words = [word for word in words if len(word) > 2]

        word_frequency = Counter(words)

        most_common_word = word_frequency.most_common(1)

        return most_common_word[0][0] if most_common_word else None

    def get_and_display_data(self):
        if not self.file_path:
            print("Выберите файл Word перед получением данных.")
            return

        result = self.most_frequent_word(self.file_path)
        self.text_result.clear()
        self.text_result.insertPlainText(f"Самое частое слово в документе: {result}")

    def load_word_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл Word", "", "Word files (*.docx);;All Files (*)")

        if file_path:
            self.file_path = file_path
            self.text_result.clear()
            self.text_result.insertPlainText(f"Выбран файл: {self.file_path}")


if __name__ == "__main__":
    app = QApplication([])
    word_app = WordApp()
    word_app.show()
    app.exec()
