"""
  1.5 There are three types of edits that can be performed on strings: insert a
    character, remove a character, or replace a character. Given two strings, 
    write a function to check if they are one or fewer edits away.
"""

"""
  Let's note that removing and inserting a character are functionally equivalent
  from the point of view of an edit.
  "pale" can be transformed to "ple" by removing a character, thus "ple" can be
  transformed to "pale" by inserting a character. 
  If we just need to know whether or not two strings can be transformed this way
  checking both insertion and removal of a character is redundant.
"""


def check_one_away(one: str, two: str) -> bool:
    """Checks if string one and string two differ by fewer than one inserts or
    replacements of characters

    Args:
        one (str):              string one to check against string two
        two (str):              string two to check against string one

    Returns:
        bool:                   if the strings are fewer than one edit different
    """

    if one == two:
        # The strings are the same
        return True
    elif abs(len(one) - len(two)) > 1:
        # The strings are too different by length
        return False
    elif len(one) == len(two):
        return single_replace(one, two)

    return single_insert(one, two) or single_insert(two, one)


def single_replace(one: str, two: str) -> bool:
    return sum(char_one != char_two for char_one, char_two in zip(one, two)) == 1


def single_insert(one: str, two: str) -> bool:
    inserts_allowed = 1
    i, j = 0, 0

    while i < len(one) and j < len(two):
        if one[i] != two[j]:
            if inserts_allowed == 0:
                return False
            inserts_allowed -= 1
        else:
            i += 1
        j += 1

    return True
