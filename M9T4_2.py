# Задача "Функциональное разнообразие":
"""
Lambda-функция:
    Даны 2 строки:
        first = 'Мама мыла раму'
        second = 'Рамена мало было'
    Необходимо составить lambda-функцию для следующего выражения -
        list(map(?, first, second)).
        Здесь ? - место написания lambda-функции.

Замыкание:
    Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
        Внутри этой функции, напишите ещё одну - write_everything(*data_set),
            где *data_set - параметр принимающий неограниченное количество данных любого типа.
        Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
    Функция get_advanced_writer возвращает функцию write_everything.

Метод __call__:
    Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
        В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words
            и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции
            можете использовать функцию choice из модуля random.
"""

# Решение (Lambda-функция):
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(
    list(
        map(
            lambda x, y: x == y,
            first, second
        )
    )
)
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]


# Решение (Замыкание):
def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file_name, 'wb') as file:
            for data in data_set:
                file.write(str(data).encode('utf-8'))
                file.write('\n'.encode('utf-8'))
    return write_everything


write = get_advanced_writer('M9T4_2.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
# Ожидаемое содержимое файла:
# Это строчка
# ['А', 'это', 'уже', 'число', 5, 'в', 'списке']


# Решение (Метод __call__):
from random import choice


class MysticBall:
    def __init__(self, *args):
        self.words = args

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное
