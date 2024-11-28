from unittest import TestCase
import sumofnumbers1
import sumofnumbers2
import largestelement
import runningtotal
import palindromechecker
import reversedelement
import listconcatenation
import elementsalternation
import integerlist
import primenumber
import evennumber

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
        listconcatenation.get_listconcatenation(["a", "b", "c", "d", "e", "f"], [1, 2, 3])
    def test_that_listconcatenation_returns_correct_value(self):
        actual = listconcatenation.get_listconcatenation(["a", "b", "c", "d", "e", "f"], [1, 2, 3])
        expected = ["a", "b", "c", "d", "e", "f", "1", "2", "3"]
        self.assertEqual(actual, expected)
    def test_that_listconcatenation_returns_correct_value_if_length_of_each_string_is_more_than_one(self):
        actual = listconcatenation.get_listconcatenation(["john", "philip", "mercy", "ben", "pat", "felix"], [35, 45, 23])
        expected = ["john", "philip", "mercy", "ben", "pat", "felix", "35", "45", "23"]
        self.assertEqual(actual, expected)
    def test_that_elementsalternation_exists(self):
        elementsalternation.get_elementsalternation(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
    def test_that_elementsalternation_returns_correct_value(self):
        actual = elementsalternation.get_elementsalternation(["a", "b", "c", "d", "e"], [1, 2, 3, 4, 5])
        expected = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5]
        self.assertEqual(actual, expected)
    def test_that_integerlist_exists(self):
        integerlist.get_integerlist(12345)
    def test_that_primenumber_exists(self):
        primenumber.get_primenumber(3)
    def test_that_primenumber_returns_correct_value(self):
        actual = primenumber.get_primenumber(3)
        expected = True
        self.assertEqual(actual, expected)
    def test_that_evennumber_exists(self):
        evennumber.get_evennumber(self)
            pass 












