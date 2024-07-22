"""
Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
   - Тип объекта.
   - Атрибуты объекта.
   - Методы объекта.
   - Модуль, к которому объект принадлежит.
   - Другие интересные свойства объекта, учитывая его тип (по желанию).
"""
# Решение:
import inspect


def introspection_info(obj):
    info = dict()
    info['Тип'] = type(obj).__name__
    info['Методы'] = [x[0] for x in inspect.getmembers(obj) if 'method' in str(x[1])]
    info['Аттрибуты'] = [x for x in dir(obj) if x not in info['Методы']]
    info['Модуль'] = inspect.getmodule(obj).__name__ if inspect.getmodule(obj) else None
    # info['Документация'] = inspect.getdoc(obj)
    return info


if __name__ == '__main__':
    # Проверочный код:
    number_info = introspection_info(42)
    print(number_info)

    # Ожидаемый вывод:
    # {'type': 'int', 'attributes': ['__abs__', '__add__', ...], 'methods': [], 'module': '__main__'}

