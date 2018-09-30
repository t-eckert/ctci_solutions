import unittest
import q5_One_Away


class TestOneAway(unittest.TestCase):
    def test_check_one_away_with_insert(self):
        test_value_1 = "ple"
        test_value_2 = "pale"
        self.assertTrue(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_deletion(self):
        test_value_1 = "Code"
        test_value_2 = "ode"
        self.assertTrue(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_same(self):
        test_value_1 = "word"
        test_value_2 = "word"
        self.assertTrue(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_replacement(self):
        test_value_1 = "hay"
        test_value_2 = "hey"
        self.assertTrue(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_false_len_diff(self):
        test_value_1 = "cool"
        test_value_2 = "hot"
        self.assertFalse(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_false_replacement(self):
        test_value_1 = "energy"
        test_value_2 = "matter"
        self.assertFalse(q5_One_Away.check_one_away(test_value_1, test_value_2))

    def test_check_one_away_with_false_big_len_diff(self):
        test_value_1 = "a"
        test_value_2 = "abcdefg"
        self.assertFalse(q5_One_Away.check_one_away(test_value_1, test_value_2))