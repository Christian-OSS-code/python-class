from unittest import TestCase
import reversedelement

class TestReversedElement(TestCase):
    def test_that_reversedelement_exists(self):
        reversedelement.get_reversedelement([1, 3, 5, 9, 11])   
    def test_that_reversedelement_returns_correct_value(self):
        actual = reversedelement.get_reversedelement([1, 3, 5, 9, 11])
        expected = [11, 9, 5, 3, 1]
        self.assertEqual(actual, expected)
    def test_that_reversedelement_returns_correct_value_for_negative_inputs(self):
        actual = reversedelement.get_reversedelement([-1, -3, -2, -7])
        expected = [-7, -2, -3, -1]
        self.assertEqual(actual, expected)
