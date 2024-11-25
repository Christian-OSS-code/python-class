from unittest import TestCase
import palindromechecker

class TestPalindromeChecker(TestCase):
    def test_that_palindromechecker_exists(self):
        palindromechecker.get_palindromechecker("madam")
    def test_that_palindromechecker_returns_correct_value(self):
        actual = palindromechecker.get_palindromechecker("madam")
        expected = True 
        self.assertEqual(actual, expected)
    def test_that_palindromechecker_returns_correct_value_for_even_number_inputs(self):
        actual = palindromechecker.get_palindromechecker("boob")
        expected = True
        self.assertEqual(actual, expected)
    def test_that_palindromechecker_returns_correct_for_integer_expressed_as_strings(self):
        actual = palindromechecker.get_palindromechecker("543212345")
        expected = True
        self.assertEqual(actual, expected)
