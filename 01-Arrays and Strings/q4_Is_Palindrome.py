"""
1.4 Palindrome Permutation: Given as string, write a function to check if it is
    a permutation of a palindrome. The palindrome does not need to be limited
    to just dictionary words. 

    EXAMPLE:
    input = Tact Coa
    output = True 
    There exist permutation of the string 'tactcoa' that are palidromes (i.e. 'tacocat')
"""

# Let's begin by thinking of what qualifies a list of values as a palindrome.
# Each value must have a pair exempting one if the length of the list is odd.


def check_palindrome_permute(chars):
    """
    Checks if a given string or list is a permutation of a palindrome
    """
    chars = chars.replace(" ", "").lower()
    unmatched_char_allowed = len(chars) % 2 != 0
    for char in chars:
        if chars.count(char) % 2 != 0:
            if unmatched_char_allowed:
                unmatched_char_allowed = False
            else:
                return False
    return True
