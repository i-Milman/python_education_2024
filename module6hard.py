import math


class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = True

    def __init__(self, color, *sides):
        # Небольшой фикс из-за особенностей инициализации некоторых фигур
        # с одним числом сторон (например, квадрат, круг, куб, пирамида и т.д.)
        if len(sides) == 1 and isinstance(sides[0], tuple):
            sides = sides[0]
        if not self.set_sides(*sides):
            sides = [1] * self.sides_count
            self.set_sides(*sides)
        if not self.set_color(*color):
            self.filled = False

    def get_color(self):
        """ Отображение значения защищённого свойства '__color' """
        # Единственное найденное полезное применение ранее созданного свойства 'filled'
        return self.__color if self.filled else None

    def get_sides(self):
        """ Отображение значения защищённого свойства '__sides' """
        return self.__sides

    def __is_valid_color(self, *colors) -> bool:
        """ Служебный метод класса, проверяющий возможность изменения цвета заливки фигуры """
        if not len(colors) == 3:
            return False
        for color in colors:
            if not 0 <= color <= 255:
                return False
        return True

    def __is_valid_sides(self, *sides) -> bool:
        """ Служебный метод класса, проверяющий возможность изменения сторон фигуры """
        if not len(sides) == self.sides_count:
            return False
        for num in sides:
            if num < 0:
                return False
        return True

    def set_color(self, *colors):
        """ Установка цвета заливки фигуры, используется как при инициализации объекта, так и при работе с объектом """
        if not self.__is_valid_color(*colors):
            return False
        self.__color = [*colors]
        return True

    def set_sides(self, *sides):
        """ Установка сторон фигуры, используется как при инициализации объекта, так и при работе с объектом """
        if not self.__is_valid_sides(*sides):
            return False
        self.__sides = [*sides]
        return True

    def __len__(self):
        """ Вывод суммы сторон фигуры """
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        self.__radius = None
        self.__square = None
        super().__init__(color, sides)

    def set_sides(self, *sides):
        if super().set_sides(*sides):
            self.__radius = self.get_sides()[0] / (2 * math.pi)
            self.__square = math.pi * self.__radius ** 2
            return True
        return False

    def get_square(self):
        return self.__square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        self.__square = None
        self.__height = None
        super().__init__(color, sides)

    def set_sides(self, *sides):
        if super().set_sides(*sides):
            p = sum(self.get_sides()) / 2
            self.__square = math.sqrt(
                p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
            self.__height = 2 * self.__square / self.get_sides()[0]
            return True
        return False

    def get_square(self):
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        self.__volume = None
        sides = [*sides] * self.sides_count
        super().__init__(color, *sides)

    def set_sides(self, *sides):
        if super().set_sides(*sides):
            self.__volume = self.get_sides()[0] ** 3
            return True
        return False

    def get_volume(self):
        # Есть альтернатива: math.pow(self.get_sides()[0], 3)
        return self.__volume


# Код для проверки:
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Дополнительно
print()
circle2 = Circle((200, 200, 100), 10, 15, 6)  # его стороны будут - [1]
print(circle2.get_sides())
triangle2 = Triangle((200, 200, 100), 10, 6)  # его стороны будут - [1, 1, 1]
print(triangle2.get_sides())
cube2 = Cube((200, 200, 100), 9)  # его стороны будут - [9, 9, 9, ....., 9]
print(cube2.get_sides())
cube3 = Cube((200, 200, 100), 9, 12)  # его стороны будут - [1, 1, 1, ....., 1]
print(cube3.get_sides())

print()
print(circle2.get_square())
print(triangle2.get_square())
print(cube2.get_volume())
