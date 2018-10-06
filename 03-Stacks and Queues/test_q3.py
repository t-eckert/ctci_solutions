import unittest
from q3_Stack_of_Plates import SetOfStacks


class TestStackOfPlates(unittest.TestCase):
    def test_push_to_stack(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_stack = [1]

        # act
        test_stacks.push(1)

        # assert
        self.assertEqual(expected_stack, test_stacks.peek())

    def test_push_to_stack_overflow(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_stack_0 = [1, 2, 3]
        expected_stack_1 = [4]

        # act
        for i in range(1, 5):
            test_stacks.push(i)

        # assert
        self.assertEqual(expected_stack_1, test_stacks.peek())

    def test_pop_from_stack(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_value = 1

        # act
        test_stacks.push(1)

        # assert
        self.assertEqual(expected_value, test_stacks.pop())

    def test_pop_from_stack_overflow(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_stack_0 = [1, 2, 3]
        expected_stack_1 = [4]

        # act
        for i in range(1, 5):
            test_stacks.push(i)

        # assert
        self.assertEqual(expected_stack_1[0], test_stacks.pop())
        self.assertEqual(expected_stack_0[2], test_stacks.pop())
        self.assertEqual(expected_stack_0[1], test_stacks.pop())
        self.assertEqual(expected_stack_0[0], test_stacks.pop())

    def test_pop_from_empty(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_response = "Set of stacks is empty."

        # act

        # assert
        self.assertEqual(expected_response, test_stacks.pop())

    def test_peek_at_empty(self):
        # arrange
        test_threshold = 3
        test_stacks = SetOfStacks(test_threshold)

        expected_response = "Set of stacks is empty."

        # act

        # assert
        self.assertEqual(expected_response, test_stacks.peek())
