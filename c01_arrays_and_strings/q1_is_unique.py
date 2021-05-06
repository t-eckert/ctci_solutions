"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique 
    characters. What if you cannot use additional data structures?
"""

"""
Because Python doesn't require a type definition for the input of a function,
we can be clever and write a function that will determine the "uniqueness" of 
a string or a list depending on what is input. 
"""

from typing import Iterable

"""
If we're going to write check_unique without any additional data
structures we can use the count() method in Python. We iterate
through the values in the input and check the number of occurances
of that value in the array.
"""


def are_items_unique_iter(items: Iterable) -> bool:
    """True if input has no repeated values. False otherwise.

    Args:
        items (Iterable):       iterable items whose uniqueness will be checked

    Returns:
        bool:                   whether the items in the iterable are unique
    """

    return all(items.count(item) == 1 for item in items)


"""
We can alternatively use Python's set function.
"""


def are_items_unique_set(items: Iterable) -> bool:
    """True if input has no repeated values. False otherwise.

    Args:
        items (Iterable):       iterable items whose uniqueness will be checked

    Returns:
        bool:                   whether the items in the iterable are unique
    """

    return len(items) == len(set(items))
