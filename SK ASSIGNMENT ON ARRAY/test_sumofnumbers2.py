from unittest import TestCase
import sumofnumbers1
import sumofnumbers2
import largestelement
import runningtotal
import palindromechecker
import reversedelement
import listconcatenation

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
    def test_that_sumofnumbers2_returns_correct_value_with_positive_inputs(self):
        actual = sumofnumbers2.get_sumofnumbers2([3, 7, 4, 12, 31])
        expected = 57
        self.assertEqual(actual, expected)
    def test_that_sumofnumbers2_returns_correct_value_with_negative_inputs(self):
        actual = sumofnumbers2.get_sumofnumbers2([-3, -7, -4, -12, -31])
        expected = -57
        self.assertEqual(actual, expected)
    def test_that_sumofnumbers2_returns_correct_value_for_all_zero_inputs(self):
        actual = sumofnumbers2.get_sumofnumbers2([0, 0, 0, 0, 0, 0])
        expected = 0
        self.assertEqual(actual, expected)

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

    def test_that_listconcatenation_exists(self): 
        listconcatenation.get_concatenation([a, b, c, e, f], [1, 2, 3, 4])














