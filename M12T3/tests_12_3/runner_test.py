"""
Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
    Далее вызовите метод walk у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
    Далее вызовите метод run у этого объекта 10 раз.
    После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
    Далее 10 раз у объектов вызываются методы run и walk соответственно.
    Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.
"""


import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_obj = runner.Runner('Horse')
        [test_obj.walk() for _ in range(10)]
        self.assertEqual(test_obj.distance, 50)

    def test_run(self):
        test_obj = runner.Runner('Wolf')
        [test_obj.run() for _ in range(10)]
        self.assertEqual(test_obj.distance, 100)

    def test_challenge(self):
        test_obj_1 = runner.Runner('Dog')
        [test_obj_1.walk() for _ in range(10)]

        test_obj_2 = runner.Runner('Cat')
        [test_obj_2.run() for _ in range(10)]

        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    unittest.main()
