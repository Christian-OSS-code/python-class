from unittest import TestCase
import creditcardcheckerexistence
import typevisacard
import typemastercard
import typediscoverycard
import typeamericanexpresscard
import doubleseconddigitofcreditcard
import adddoubledigits
import sumofdigitsinprevioustest
import sumofdigitsatoddindex
import sumofvaluesofdigitsinlasttwotests


class TestCreditCardCheckerExistence(TestCase):
    def test_that_creditcardcheckerexistence_exists(self):
        creditcardcheckerexistence.get_creditcardcheckerexistence(4388576018402626)



    def test_that_the_length_of_credit_card_is_within_the_required_range(self):
        actual = creditcardcheckerexistence.get_creditcardcheckerexistence(4388576018402626)
        expected = "Length of card number is within range"
        self.assertEqual(actual, expected)


        actual = creditcardcheckerexistence.get_creditcardcheckerexistence(438857601840)
        expected = "Length of card number out of range"
        self.assertEqual(actual, expected)


    def test_that_credit_card_is_type_visa_card_if_the_first_digit_is_four(self):
        actual = typevisacard.get_typevisacard([4, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6])
        expected = "Visa Cards"
        self.assertEqual(actual, expected)


    def test_that_credit_card_is_master_card_according_to_specification(self):
        actual = typemastercard.get_typemastercard([5, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6])
        expected = "Master Card"
        self.assertEqual(actual, expected)


    def test_that_credit_card_is_discovery_card_aaccording_to_specification(self):
        actual = typediscoverycard.get_typediscoverycard([6, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6])
        expected = "Discovery Card"
        self.assertEqual(actual, expected)


    def test_that_credit_card_is_American_Express_Card_if_first_and_second_digits_are_three_and_seven_respectively(self):
        actual = typeamericanexpresscard.get_typeamericanexpresscard([3, 7, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6])
        expected = "American Express Card"
        self.assertEqual(actual, expected)

    
    def test_on_doubling_second_digit_from_right_to_left(self):
        actual = doubleseconddigitofcreditcard.get_doubleseconddigitofcreditcard(4388576018402626)
        expected = [4, 4, 8, 2, 12, 10, 16, 8]
        self.assertEqual(actual, expected)



    def test_to_add_the_credit_card_digits_that_are_double_and_return_their_results(self):
        actual = adddoubledigits.get_adddoubledigits(4388576018402626)
        expected = [4, 4, 8, 2, 3, 1, 7, 8]
        self.assertEqual(actual, expected)


    def test_that_sumofdigitsinprevioustest_returns_correct_value(self):
        actual = sumofdigitsinprevioustest.get_sumofdigitsinprevioustest(4388576018402626)
        expected = 37
        self.assertEqual(actual, expected)

        
        
    def test_that_sumofdigitsatoddindex_returns_correct_value(self):
        actual = sumofdigitsatoddindex.get_sumofdigitsatoddindex(4388576018402626)
        expected = 38
        self.assertEqual(actual, expected)


    def test_that_sumofvaluesofdigitsinlasttwotests_returns_correct_value(self):
        actual = sumofvaluesofdigitsinlasttwotests.get_sumofvaluesofdigitsinlasttwotests(4388576018402626)
        expected = 75
        self.assertEqual(actual, expected)
        












