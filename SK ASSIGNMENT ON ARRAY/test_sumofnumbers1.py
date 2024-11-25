from unittest import TestCase
import sumofnumbers1
import sumofnumbers2

class TestSumOfNumbers1(TestCase):
    def test_that_sumofnumbers1_exists(self):
        sumofnumbers1.get_sumofnumbers1([2, 3, 10, 11, 13])
    def test_that_sumofnumbers1_returns_correct_value(self):
        actual = sumofnumbers1.get_sumofnumbers1([2, 3, 10, 11, 13])
        expected = 39
        self.assertEqual(actual, expected)
    def test_that_sumofnumbers1_returns_correct_value_for_all_zero_inputs(self):
        actual = sumofnumbers1.get_sumofnumbers1([0, 0, 0, 0, 0, 0])
        expected = 0
        self.assertEqual(actual, expected)

    def test_that_sumofnumbers2_exists(self):
        sumofnumbers2.get_sumofnumbers2([3, 7, 4, 12, 31])
