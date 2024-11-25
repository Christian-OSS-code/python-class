from unittest import TestCase
import runningtotal

class TestRunningTotal(TestCase):
    def test_that_runningtotal_exists(self):
        runningtotal.get_runningtotal([2, 3, 6, 7, 8])
    def test_that_runningtotal_returns_correct_value(self):
        actual = runningtotal.get_runningtotal([2, 3, 6, 7, 8])
        expected = 26
        self.assertEqual(actual, expected)
    def test_that_runningtotal_returns_correct_value_for_negative_inputs(self):
        actual = runningtotal.get_runningtotal([-2, -3, -6, -7, -8])
        expected = -26
        self.assertEqual(actual, expected)
