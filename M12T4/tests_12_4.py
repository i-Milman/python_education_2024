import logging
import unittest

import rt_with_exceptions as runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            test_obj = runner.Runner('Horse', -2)
            [test_obj.walk() for _ in range(10)]
            self.assertEqual(test_obj.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            test_obj = runner.Runner(-2)
            [test_obj.run() for _ in range(10)]
            self.assertEqual(test_obj.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        test_obj_1 = runner.Runner('Dog')
        [test_obj_1.walk() for _ in range(10)]

        test_obj_2 = runner.Runner('Cat')
        [test_obj_2.run() for _ in range(10)]

        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s', encoding='UTF-8')

unittest.main()
