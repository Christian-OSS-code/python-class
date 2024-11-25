from unittest import TestCase
import largestelement

class TestLargestElement(TestCase):
    def test_that_largestelement_exists(self):
        largestelement.get_largestelement([2, 4, 9, 3])
    def test_that_largestelement_returns_correct_value(self):
        actual = largestelement.get_largestelement([2, 4, 9, 3])
        expected = 9
        self.assertEqual(actual, expected)
    def test_that_largestelement_returns_correct_value_for_negative_inputs(self):
        actual = largestelement.get_largestelement([-1, -5, -2, -9])
        expected = -1
        self.assertEqual(actual, expected)
    def test_that_largestelement_returns_correct_value_for_all_zero_inputs(self):
        actual = largestelement.get_largestelement([0, 0, 0, 0])
        expected = 0
        self.assertEqual(actual, expected)
