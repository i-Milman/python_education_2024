# Задача:
"""
Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки,
используя оператор yield.
В функцию передаётся только сама строка.
"""

# Решение:
def all_variants(text: str):
    """ Генерирует все подпоследовательности переданной строки. """
    for last in range(len(text) + 1):
        for first in range(last):
            yield text[first:last]

# Проверка:
a = all_variants("abc")
for i in a:
    print(i)

a = all_variants('12345')
for i in a:
    print(i)