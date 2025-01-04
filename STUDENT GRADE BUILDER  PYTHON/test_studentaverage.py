from unittest import TestCase

import studentgrade
import studenttotal
import studentaverage

class TestStudentGrade(TestCase):

    def test_that_studentgrade_exists(self):
        studentgrade.get_studentgrade({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})


    def test_that_studentgrade_returns_correctvalue_for_total_score(self):
        actual = studentgrade.get_studentgrade({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = 426

        self.assertEqual(actual, expected)

    def test_that_studenttotal_returns_correctvalue_for_student_total(self):
        actual = studenttotal.get_studenttotal({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [70, 140, 216]
        self.assertEqual(actual, expected)

    def test_that_student_average_returns_correct_value(self):
        actual = studentaverage.get_studentaverage({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]}, 3)
        expected = [23.33, 46.67, 72.00]
        self.assertEqual(actual, expected)



















