# Задача "Потоки гостей в кафе":

# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
# Класс Table:
#   Объекты этого класса должны создаваться следующим способом - Table(1)
#   Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
# Класс Guest:
#   Должен наследоваться от класса Thread (быть потоком).
#   Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
#   Обладать атрибутом name - имя гостя.
#   Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.
# Класс Cafe:
#   Объекты этого класса должны создаваться следующим способом - Guest(Table(1), Table(2),....)
#   Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
#   Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
# Метод guest_arrival(self, *guests):
#   Должен принимать неограниченное кол-во гостей (объектов класса Guest).
#   Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest),
#   запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
#   Если же свободных столов для посадки не осталось,
#   то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
# Метод discuss_guests(self):
#   Этот метод имитирует процесс обслуживания гостей.
#   Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
#       Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive),
#           то вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)"
#           и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
#       Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None),
#           то текущему столу присваивается гость взятый из очереди (queue.get()).
#           Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
#           Далее запустить поток этого гостя (start)
#       Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
#       Table - стол, хранит информацию о находящемся за ним гостем (Guest).
#       Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
#       Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival)
#       и их обслуживания (discuss_guests).

# Решение:
from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        """
        ожидание случайным образом от 3 до 10 секунд
        :return:
        """
        super().run()
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):
        """
        прибытие гостей
        :return:
        """
        free_tables = len(self.tables)
        for guest in guests:
            if not free_tables:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            free_tables -= 1

    def discuss_guests(self):
        """
        обслужить гостей
        :return:
        """
        while any(table.guest is not None for table in self.tables) or not self.queue.empty():
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                        print(f'Стол номер {table.number} свободен')
                        table.guest.join()
                        if not self.queue.empty():
                            table.guest = self.queue.get()
                            table.guest.start()
                            print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        else:
                            table.guest = None
            sleep(0.1)


# Проверка:
if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
