"""
lab8_test.py

Name: Kaiqin Huang
Date: 1/17/2017

A module of test functions for count_merge(), count_as(), and split_evens().
"""


import unittest
import lab8

class TestLab8(unittest.TestCase):

    def test_count_merge(self):
        self.assertEqual(lab8.count_merge({1,2,3}, {3,4,5}), 5, "The size of the merged set is 5.")
        self.assertEqual(lab8.count_merge({1,2,3}, {2,3,4}), 4, "The size of the merged set is 5.")
        self.assertEqual(lab8.count_merge({1,2,3,4}, {3,4,5}), 5, "The size of the merged set is 5.")
        self.assertEqual(lab8.count_merge({1,2,3,4,5}, {3,4,5}), 5, "The size of the merged set is 5.")

    def test_count_as(self):
        self.assertEqual(lab8.count_as(["Apple", "Python", "Tuesday"]), 1, "Lower case letter 'a' appears twice.")
        self.assertEqual(lab8.count_as(["Apple", "Python"]), 0, "Lower case letter 'a' appears once.")
        self.assertEqual(lab8.count_as(["Apple", "Python", "Solvang"]), 1, "Lower case letter 'a' appears twice.")
        self.assertEqual(lab8.count_as(["Apple", "Python", "Tuesday", "Solvang"]), 2, "Lower case letter 'a' appears three times.")

    def test_split_evens(self):
        test_list = [1,2,3,4,5,6,7,8,9,10]

        test_evens, test_odds = lab8.split_evens(test_list)
        self.assertIn(2, test_evens)
        self.assertNotIn(3, test_evens)
        self.assertIn(9, test_odds)
        self.assertNotIn(10, test_odds)

