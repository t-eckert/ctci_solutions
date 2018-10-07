import unittest
from q1_sorted_merge import merge_sorted_lists 

class TestSortedMerge(unittest.TestCase):
    def test_merge_sorted_lists(self):
        # arrange
        test_list_A = [2, 3, 5, None, None, None]
        test_list_B = [1, 4, 9]

        expected_list = [1, 2, 3, 4, 5, 9]

        # act
        merged_list = merge_sorted_lists(test_list_A, test_list_B)

        # assert
        self.assertEqual(expected_list, merged_list)

    def test_buffer_too_small(self):
        # arrange
        test_list_A = [2, 3, 5, None, None]
        test_list_B = [1, 4, 9]

        expected_response = None

        # act
        none_response = merge_sorted_lists(test_list_A, test_list_B)

        # assert
        self.assertEqual(expected_response, none_response)
