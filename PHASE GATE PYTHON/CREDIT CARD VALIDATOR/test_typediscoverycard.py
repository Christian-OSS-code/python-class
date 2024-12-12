from unittest import TestCase
import creditcardcheckerexistence
import typevisacard
import typemastercard
import typediscoverycard
import typeamericanexpresscard


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














