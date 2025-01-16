# Задание №3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# Show() — вывод на экран информации о фигуре;
# Save() — сохранение фигуры в файл;
# Load() — считывание фигуры из файла.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого верхнего угла и
# длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и
# размерами;
# 2
# Circle — окружность с заданными координатами центра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего угла, описанного вокруг него
# прямоугольника со сторонами, параллельными осям координат, и размерами этого
# прямоугольника. Создайте список фигур, сохраните фигуры в файл, загрузите в другой список
# и отобразите информацию о каждой из фигур

import pickle

class Shape:
    def __init__(self):
        pass

    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

class Square(Shape):
    def __init__(self, x, y, side_length):
        super().__init__()
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square at ({self.x}, {self.y}) with side length {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Ellipse at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

# Создаем список фигур
shapes = [
    Square(0, 0, 5),
    Rectangle(2, 3, 4, 6),
    Circle(1, 1, 3),
    Ellipse(5, 5, 6, 4)
]


with open('shapes_file.txt', 'wb') as file:
    for shape in shapes:
        shape.save(file.name)


loaded_shapes = []
with open('shapes_file.txt', 'rb') as file:
    while True:
        try:
            loaded_shapes.append(Shape.load(file.name))
        except EOFError:
            break

for shape in loaded_shapes:
    shape.show()
