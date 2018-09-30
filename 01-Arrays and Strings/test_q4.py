import unittest
import q4_Is_Palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_check_palindrome_permute_with_False_string(self):
        test_value = "bananagram"
        self.assertFalse(q4_Is_Palindrome.check_palindrome_permute(test_value))

    def test_check_palindrome_permute_with_True_string(self):
        test_value = "Tact coa"
        self.assertTrue(q4_Is_Palindrome.check_palindrome_permute(test_value))

    def test_check_palindrome_permute_with_odd_numbered_False_string(self):
        test_value = "languid"
        self.assertFalse(q4_Is_Palindrome.check_palindrome_permute(test_value))