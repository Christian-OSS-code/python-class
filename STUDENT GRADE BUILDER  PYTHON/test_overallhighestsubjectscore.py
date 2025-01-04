from unittest import TestCase

import studentgrade
import studenttotal
import studentaverage
import studentposition
import highestinsubjects
import lowestinsubjects
import totalscoreinsubjects
import averagescoreinsubjects
import numberofpasses
import numberoffailures
import higheststudentinsubject
import loweststudentinsubject
import hardestsubject
import easiestsubject
import overallhighestsubjectscore



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


    def test_that_student_grade_returns_correct_position_to_all_students(self):
        actual = studentposition.get_studentposition({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [3, 2, 1]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_subjects_with_highest_score(self):
        actual = highestinsubjects.get_highestinsubjects({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [90, 90, 76]
        self.assertEqual(actual, expected)

    def test_that_student_grade_returns_subjects_lowest_score(self):
        actual = lowestinsubjects.get_lowestinsubjects({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [10, 20, 20]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_total_subject_scores(self):
        actual = totalscoreinsubjects.get_totalscoreinsubjects({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [130, 160, 136]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_correct_subject_average_scores(self):
        actual = averagescoreinsubjects.get_averagescoreinsubjects({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = ["43.33", "53.33", "45.33"]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_correct_number_of_student_that_passed(self):
        actual = numberofpasses.get_numberofpasses({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [1, 2, 1]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_correct_number_of_student_that_failed(self):
        actual = numberoffailures.get_numberoffailures({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [2, 1, 2]
        self.assertEqual(actual, expected)



    def test_that_student_grade_returns_correct_highest_student_score_in_subjects(self):
        actual = higheststudentinsubject.get_higheststudentinsubject({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [[3], [2], [3]]
        self.assertEqual(actual, expected)


    def test_that_student_graed_returns_correct_lowest_student_score_in_subjects(self):
        actual = loweststudentinsubject.get_loweststudentinsubject({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [[2], [1], [1]]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_hardest_subject(self):
        actual = hardestsubject.get_hardestsubject({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [1, 3]
        self.assertEqual(actual, expected)


    

    def test_that_student_grade_returns_easiest_subject(self):
        actual = easiestsubject.get_easiestsubject({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = [2]
        self.assertEqual(actual, expected)


    def test_that_student_grade_returns_overall_highest_score(self):
        actual = overallhighestsubjectscore.get_overallhighestsubjectscore({"student 1": [30, 20, 20], "student 2": [10, 90, 40], "student 3": [90, 50, 76]})
        expected = 90
        self.assertEqual(actual, expected)
    





































