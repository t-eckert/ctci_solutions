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


def check_one_away(s1, s2):
    if s1 == s2:
        return True
    elif len(s1) == len(s2):
        return check_replace(s1, s2)
    elif len(s1) == len(s2) + 1 or len(s1) == len(s2) - 1:
        return check_remove(s1, s2)
    else:
        return False


def check_replace(s1, s2):
    diff_allowed = True
    for s1_char, s2_char in zip(s1, s2):
        if s1_char != s2_char:
            if diff_allowed:
                diff_allowed = False
            else:
                return False
    return True


def check_remove(s1, s2):
    diff = 0
    s_shorter, s_longer = (s1, s2) if len(s1) < len(s2) else (s2, s1)
    for i, char in enumerate(s_longer):
        diff += 1 if char != s_shorter[i + diff] else 0
        if diff > 1:
            return False
    return True

