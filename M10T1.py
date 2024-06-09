# Задача:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.

# Решение:
from time import sleep
from threading import Thread, Lock

# "with lock:" добавлено в обе функции как заплатка для соответствия эталлону решению,
# иначе возникает проблема вывода данных в один поток stdout, что приводит к перемешиванию вывода.
lock = Lock()


def print_nums():
    for num in range(1, 11):
        with lock:
            print(str(num))
        sleep(1)


def print_chars():
    for char in range(ord('a'), ord('j') + 1):
        with lock:
            print(chr(char))
        sleep(1)


thread_1 = Thread(target=print_nums)
thread_2 = Thread(target=print_chars)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
