# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте


class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    pass


def throw_exception(arg1, arg2):
    if arg1 > arg2:
        raise InvalidDataException("Неверные данные")
    elif arg1 == arg2:
        raise ProcessingException("Ошибка обработки")


def f(a, b):
    try:
        throw_exception(a, b)
        return a + b
    except (InvalidDataException, ProcessingException) as e:
        print(f"Сработало исключение: {e}")


# проверка обработки исключения
f(5, 4)
f(5, 5)

# проверка срабатывания исключения
throw_exception(5, 3)
