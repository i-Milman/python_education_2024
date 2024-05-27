print('Задача 1: Фабрика Функций')
# Написать функцию, которая возвращает различные математические функции
# (например, деление, # умножение) в зависимости от переданных аргументов.

# Решение
def make_func(operation):
    def mul(x, y):
        return x * y

    def div(x, y):
        try:
            return x / y
        except ZeroDivisionError as e:
            print(f'Ошибка: {e.__str__()}. ', end='')

    def summ(x, y):
        return x + y

    def diff(x, y):
        return x - y

    match operation:
        case '*':
            return mul
        case '/':
            return div
        case '+':
            return summ
        case '-':
            return diff
        case _:
            return None

# Проверка
func = make_func('-')
print(func(20, 4))
func = make_func('*')
print(func(9, 4))
func = make_func('/')
print(func(7, 0))


print('Задача 2: Лямбда-Функции')
# Использовать лямбда-функцию для реализации простой операции
# и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат

# Решение
def sq(x):
    return x * x

sq2 = lambda x: x * x

# Проверка
print(sq(6))
print(sq2(6))


print('Задача 3: Вызываемые Объекты')
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

# Решение
class Square:
   def __init__(self, a, b):
       self.a = a
       self.b = b
   def __call__(self):
       return self.a * self.b

# Проверка
a, b = 5, 4
print(f'Стороны: {a}, {b}')
square = Square(a, b)
print(f'Площадь: {square()}')

