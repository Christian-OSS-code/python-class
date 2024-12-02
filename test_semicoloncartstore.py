from unittest import TestCase
import semicolonstorename
import semicolonproduct
import semicolonprice
import semicolonquantity
#import semicoloncartstore

class TestSemicolonStorename(TestCase):
    def test_that_semicolonstorename_exists(self):

        pass 
    def test_that_semicolonstorename_accepts_correct_customer_name(self):
        actual = semicolonstorename.get_semicolonstorename("john")
        expected = "john"
        self.assertEqual(actual, expected)
    def test_that_semicolonproduct_accepts_correct_product_purchased(self):
        actual = semicolonproduct.get_semicolonproduct("television")
        expected = "television"
        self.assertEqual(actual, expected)
    def test_that_semicolonprice_accepts_correct_unit_price(self):
        actual = semicolonprice.get_semicolonprice(50000.00)
        expected = 50000.0
        self.assertEqual(actual, expected)
    def test_that_semicolonquantity_accepts_correct_quantity_of_product(self):
        actual = semicolonquantity.get_semicolonquantity(1)
        expected = 1
        self.assertEqual(actual, expected)
    def test_that_semicoloncartstore_returns_correct_value(self):
        actual = semicoloncartstore.get_semicoloncartstore("television", 50000.00, 1)
        expected = "television", 50000.00, 1
        self.assertEqual(actual, expected)


























    

