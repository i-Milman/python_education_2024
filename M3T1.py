"""
Задача "Счётчик вызовов":
Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).
"""
from random import randint, choice


def count_calls(func):
    """
    Считает количество выполнений функций, используя глобальную переменную
    :param func:  любая функция
    :return: та же функция
    """
    def wrapper(*args, **kwargs):
        globals()['calls'] += 1
        return func(*args, **kwargs)
    return wrapper


@count_calls
def string_info(string: str) -> (int, str, str):
    """
    Функция возвращает кортеж с данными
    :param string: строка
    :return: кортеж из длины указанной строки, строки в верхнем регистре, строки в нижнем регистре
    """
    return len(string), string.upper(), string.lower()


@count_calls
def is_contains(string: str, list_to_search: list) -> bool:
    """
    Функция проверяет наличие строки в списке
    :param string: строка
    :param list_to_search: список строк
    :return: логическое значение наличия строки в списке
    """
    return any(x.lower() == string.lower() for x in list_to_search)


calls = 0
# Запуск функций произвольное количество раз
for _1 in range(randint(10, 1000)):
    list_to_search = list()
    # Составление списка произвольной длины
    for _2 in range(randint(10, 1000)):
        list_of_symbols, string = list(), str()
        # Составление строки произвольной длины
        for _3 in range(randint(1, 5)):
            # Выбор произвольных символов для заполнения строки
            list_of_symbols.append(choice([
                chr(randint(65, 90)),       # Английские символы 65-90, 97-122
                chr(randint(97, 122)),
                chr(randint(1040, 1071)),   # Русские символы, 1040-1071, 1072-1103
                chr(randint(1072, 1103)),
                chr(randint(32, 42))        # Прочие символы 32-42
            ]))
        # Заполнение строки
        for char in list_of_symbols:
            string += char
        # Заполнение списка
        list_to_search.append(string)
    # Вызов функций
    func1_result = string_info(choice(list_to_search))
    func2_result = is_contains(choice(list_to_search), list_to_search)
    # print(list_to_search, func1_result, func2_result, sep='\n')
print(calls)
