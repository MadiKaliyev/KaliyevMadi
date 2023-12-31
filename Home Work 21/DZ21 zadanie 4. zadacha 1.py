# Задание №1
# Работаем с примером, приведенным на практике. Мы можем менять значения полей dia
# и h объекта за пределами класса простым присваиванием (например, a.dia = 10). При этом
# площадь никак не будет пересчитываться. Также мы можем назначить новое значение для
# площади, как простым присваиванием, так и вызовом функции make_area() с последующим
# присваиванием. Например, a.area = a.make_area(2, 3). При этом не меняются высота и диаметр.
# Защитите код от возможных логических ошибок следующим образом:
# Свойствам dia и h объекта по-прежнему можно выполнять присваивание за пределами
# класса. Однако при этом "за кулисами" происходит пересчет площади, т. е. изменение
# значения area.
# Свойству area нельзя присваивать за пределами класса. Можно только получать его
# значение.
# Подсказка: вспомните про метод __setattr__(), упомянутый в уроке про инкапсуляцию

class Circle:
    def __init__(self, dia, h):
        self.__dia = dia
        self.__h = h
        self.__area = self.make_area()

    def make_area(self):
        r = self.__dia / 2
        return 3.14 * r * self.__h

    @property
    def area(self):
        return self.__area

    def __setattr__(self, key, value):
        if key == 'dia' or key == 'h':
            if key == 'dia':
                self.__dia = value
            elif key == 'h':
                self.__h = value
            self.__area = self.make_area()
        else:
            super().__setattr__(key, value)


a = Circle(4, 5)
print(a.area)
a.dia = 23
print(a.area)
