# ООП. Инкапсуляция
# Выполните следующие задание:
# Напишите программу, в которой есть главный класс с текстовым полем. В главное классе
# должен быть метод для присваивания значения полю: без аргументов и с одним текстовым
# аргументом. Объект главного класса создаётся передачей одного текстового аргумента
# конструктору. На основе главного класса создается класса потомок. В классе-потомке нужно
# добавить числовое поле. У конструктора класса-потомка два аргумента.

class Main:
    def __init__(self, text):
        self.text = text

    def texttt(self, text = None):
        if text:
            self.text1 = text
        else:
            self.text1 = input('Введите текст: ')

class Potomok(Main):
    def __init__(self, text, chislo):
        super().__init__(text)
        self.chislo1 = chislo
    def set_chislo(self, chislo):
        self.chislo1 = chislo

    def get_chislo(self):
        return self.chislo1


Dlya_glavnogo = Potomok('Текст888',42)
print(Dlya_glavnogo.get_chislo())
Dlya_glavnogo.set_chislo(100)
print(Dlya_glavnogo.get_chislo())

