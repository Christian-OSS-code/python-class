from unittest import TestCase

import studentgrade
import studenttotal

class TestStudentGrade(TestCase):

    def test_that_studentgrade_exists(self):
        studentgrade.get_studentgrade({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})


    def test_that_studentgrade_returns_correctvalue_for_total_score(self):
        actual = studentgrade.get_studentgrade({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = 426
        self.assertEqual(actual, expected)

    

