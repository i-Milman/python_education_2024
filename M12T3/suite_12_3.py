import unittest
from tests_12_3 import runner_test, tournament_test

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tournament_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)