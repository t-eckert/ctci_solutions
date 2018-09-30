import unittest
import q1_Is_Unique


class TestIsUnique(unittest.TestCase):
    def test_are_items_unique_with_False_string(self):
        test_value = "bananagram"
        self.assertFalse(q1_Is_Unique.are_items_unique(test_value))

    def test_are_items_unique_with_True_string(self):
        test_value = "yoke"
        self.assertTrue(q1_Is_Unique.are_items_unique(test_value))

    def test_are_items_unique_with_False_list(self):
        test_value = [1, 2, 3, 1]
        self.assertFalse(q1_Is_Unique.are_items_unique(test_value))

    def test_are_items_unique_with_True_list(self):
        test_value = [1, 2, 3, 4]
        self.assertTrue(q1_Is_Unique.are_items_unique(test_value))

    def test_are_items_unique_single_datastructure_with_False_string(self):
        test_value = "bananagram"
        self.assertFalse(q1_Is_Unique.are_items_unique_single_datastructure(test_value))

    def test_are_items_unique_single_datastructure_with_True_string(self):
        test_value = "yoke"
        self.assertTrue(q1_Is_Unique.are_items_unique_single_datastructure(test_value))

    def test_are_items_unique_single_datastructure_with_False_list(self):
        test_value = [1, 2, 3, 1]
        self.assertFalse(q1_Is_Unique.are_items_unique_single_datastructure(test_value))

    def test_are_items_unique_single_datastructure_with_True_list(self):
        test_value = [1, 2, 3, 4]
        self.assertTrue(q1_Is_Unique.are_items_unique_single_datastructure(test_value))

