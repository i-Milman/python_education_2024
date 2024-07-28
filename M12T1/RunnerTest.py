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
