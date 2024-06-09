# Задача:
# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
# Каждый рыцарь должен иметь имя (name) и умение(skill).
# Умение рыцаря определяет, сколько времени потребуется рыцарю, чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.

# Решение:
from time import sleep
from threading import Thread, Lock

# "with lock:" добавлено для каждого вывода как заплатка для соответствия эталлону решению,
# иначе возникает проблема вывода данных в один поток stdout, что приводит к перемешиванию вывода.
lock = Lock()

class Knight(Thread):
    def __init__(self, name: str, skill: int, *args, **kwargs):
        super(Knight, self).__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        with lock:
            print(f'{self.name}, на нас напали!')
        days, warriors = 0, 100
        while warriors > 0:
            sleep(1)
            days += 1
            warriors -= self.skill
            with lock:
                print(f'{self.name} сражается {days} день(дня).., осталось {warriors} воинов.')
        with lock:
            print(f'{self.name} одержал победу спустя {days} дней(дня)!')



# Проверка:
knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения

knight1.start()
knight2.start()

knight1.join()
knight2.join()
print('Все битвы закончились!')
