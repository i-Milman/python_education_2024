import math


class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = True

    # Отображение значения защищённого свойства '__color'
    def get_color(self):
        # Единственное найденное полезное применение ранее созданного свойства 'filled'
        return self.__color if self.filled else None

    # Отображение значения защищённого свойства '__sides'
    def get_sides(self):
        return self.__sides

    # Служебный метод класса, проверяющий возможность изменения цвета заливки фигуры
    def __is_valid_color(self, *colors) -> bool:
        if not len(colors) == 3:
            return False
        for color in colors:
            if not 0 <= color <= 255:
                return False
        return True

    # Служебный метод класса, проверяющий возможность изменения сторон фигуры
    def __is_valid_sides(self, *sides) -> bool:
        if not len(sides) == self.sides_count:
            return False
        for num in sides:
            if num < 0:
                return False
        return True

    # Установка цвета заливки фигуры, используется как при инициализации объекта, так и при работе с объектом
    def set_color(self, *colors):
        if not self.__is_valid_color(*colors):
            return False
        self.__color = [*colors]
        return True

    # Установка сторон фигуры, используется как при инициализации объекта, так и при работе с объектом
    def set_sides(self, *sides):
        if not self.__is_valid_sides(*sides):
            return False
        self.__sides = [*sides]
        self.__update_properties()
        return True

    # Дополнительные операции рассчёта свойств фигуры после установки сторон фигуры
    def __update_properties(self):
        pass

    # Вывод суммы сторон фигуры
    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        if not self.set_sides(side):
            self.__sides = [1] * self.sides_count
        if not self.set_color(*color):
            self.filled = False

    def __update_properties(self):
        self.__radius = self.__sides[0] / (2 * math.pi)
        self.__square = math.pi * self.__radius ** 2

    def get_square(self):
        return self.__square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if not self.set_sides(*sides):
            self.__sides = [1] * self.sides_count
        if not self.set_color(*color):
            self.filled = False

    def __update_properties(self):
        p = sum(*self.__sides) / 2
        self.__square = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
        self.__height = 2 * self.__square / self.__sides[0]

    def get_square(self):
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        sides = [side] * self.sides_count
        if not self.set_sides(*sides):
            self.__sides = [1] * self.sides_count
        if not self.set_color(*color):
            self.filled = False

    def get_volume(self):
        # Есть альтернатива: math.pow(self.get_sides()[0], 3)
        return self.get_sides()[0] ** 3


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
