"""
Задача:
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить дополненный с предыдущей задачи класс Runner и новый класс Tournament.
Изменения в классе Runner:
    Появился атрибут speed для определения скорости бегуна.
    Метод __eq__ для сравнивания имён бегунов.
    Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
    Класс Tournament представляет собой класс соревнований, где есть дистанция,
    которую нужно пробежать и список участников.
    Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results.
    Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
    Бегун по имени Усэйн, со скоростью 10.
    Бегун по имени Андрей, со скоростью 9.
    Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
    У объекта класса Tournament запускается метод start, который возвращает словарь в переменную results.
    В конце вызывается метод assertTrue,
    в котором сравниваются последний объект из result и предполагаемое имя последнего бегуна (индекс -1).
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.

Дополнительно (не обязательно, не влияет на зачёт):
В данной задаче, а именно в методе start класса Tournament, допущена логическая ошибка.
    В результате его работы бегун с меньшей скоростью может пробежать некоторые дистанции быстрее, чем бегун с большей.
Попробуйте решить эту проблему и обложить дополнительными тестами.
"""

import unittest
import runner_and_tournament as rt


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def setUp(cls):
        cls.runner1 = rt.Runner("Усэйн", 10)
        cls.runner2 = rt.Runner("Андрей", 9)
        cls.runner3 = rt.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print({key_: str(value_) for key_, value_ in value.items()})

    # 3 теста по условию
    def test_usain_nick(self):
        tournament = rt.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["Усэйн и Ник"] = results

        last = results[len(results)]
        self.assertEqual(last, self.runner3)

    def test_andrey_nick(self):
        tournament = rt.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["Андрей и Ник"] = results

        last = results[len(results)]
        self.assertEqual(last, self.runner3)

    def test_usain_andrey_nick(self):
        tournament = rt.Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["Усэйн, Андрей и Ник"] = results

        last = results[len(results)]
        self.assertEqual(last, self.runner3)

    """
    # 2 теста дополнительно
    def test_usain_andrey(self):
        tournament = rt.Tournament(900, self.runner1, self.runner2)
        results = tournament.start()
        self.all_results["Усэйн и Андрей"] = results

        last = results[len(results)]
        self.assertEqual(last, self.runner2)

    def test_andrey_usain(self):
        tournament = rt.Tournament(900, self.runner2, self.runner1)
        results = tournament.start()
        self.all_results["Андрей и Усэйн"] = results

        last = results[len(results)]
        self.assertEqual(last, self.runner2)
    """



if __name__ == '__main__':
    unittest.main()
