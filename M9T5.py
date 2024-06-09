# Задача:
# Напишите 2 функции:
# Функция которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.

# Решение:
def is_prime(func):
    """
    Функция декоратор, которая распечатывает "Простое", если результат искомой функции будет простым числом
    :param func: Функция
    :return: Декорированная функция
    """

    def wrapper(*args, **kwargs):
        num = func(*args, **kwargs)
        if num == 2 or all(num % i for i in range(3, num)):
            print("Простое")
        else:
            print("Составное")
        return num

    return wrapper


@is_prime
def summ_three(first, second, third):
    """
    Функция, которая складывает 3 числа
    :param first: Первое число
    :param second: Второе число
    :param third: Третье число
    :return: Сумма
    """
    return first + second + third


# Проверка:
print(summ_three(1, 99, 3))
print(summ_three(1, 98, 3))
