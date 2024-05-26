def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exc:
        print(f'* Выполняется обработка исключения "{exc}", ', end='')
        result = str(a) + str(b)
    else:
        print('* Исключения не были вызваны, ', end='')
    finally:
        print('функция завершает свою работу')
    return result

# Пример кода:
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))