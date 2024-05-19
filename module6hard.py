import math


class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = True

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, *colors) -> bool:
        if not len(colors) == 3:
            return False
        for color in colors:
            if not 0 <= color <= 255:
                return False
        return True

    def __is_valid_sides(self, *sides) -> bool:
        if not len(sides) == self.sides_count:
            return False
        for num in sides:
            if num < 0:
                return False
        return True

    def set_color(self, *colors):
        if not self.__is_valid_color(*colors):
            return
        self.__color = [*colors]

    def set_sides(self, *sides):
        if not self.__is_valid_sides(*sides):
            return False
        self.__sides = [*sides]
        return True

    def __len__(self):
        if isinstance(self.__sides, list):
            return sum(self.__sides)
        else:
            return self.__sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, side):
        if not self.set_sides(side):
            self.__sides = [1]
        if not self.set_color(*color):
            self.__sides = [1] * 3

        self.__radius = self.__sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if not self.set_sides([*sides] * self.sides_count):
            self.__sides = [1] * self.sides_count
        if not self.set_color(*color):
            self.__sides = [1] * 3

        p = sum(*self.__sides) / 2
        self.__square = math.sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))
        self.__height = 2 * self.__square / self.__sides[0]

    def get_square(self):
        return self.__square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if not self.set_sides([*sides] * self.sides_count):
            self.__sides = [1] * self.sides_count
        if not self.set_color(*color):
            self.__sides = [1] * 3

    def get_volume(self):
        return math.prod(self.__sides)


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
