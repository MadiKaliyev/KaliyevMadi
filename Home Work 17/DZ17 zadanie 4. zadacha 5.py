# ООП. Инкапсуляция
# Выполните следующие задания:
# Задания №1
# Разработайте класс с "полной инкапсуляцией", доступ к атрибутам которого и
# изменение данных реализуются через вызовы методов. В объектно-ориентированном
# программировании принято имена методов для извлечения данных начинать со слова get
# (взять), а имена методов, в которых свойствам присваиваются значения, – со слова set
# (установить). Например, get_field, set_field


class Python:
    def __init__(self, name, age, kurs):
        self.__name = name #private
        self._age = age #protected
        self.kurs = kurs #public
    def set_x(self, name):
        self.__name = name
    def get_x(self):
        return self.__name


Student = Python('Мади', 39, 'Разработчик')
Student.set_x(name='Калиев')
Student._age = 47
Student.kurs = 'Back end Разработчик'
print(f'{Student._age}, {Student.get_x()}, {Student.kurs}')