"""
1.4 Palindrome Permutation: Given as string, write a function to check if it is
    a permutation of a palindrome. The palindrome does not need to be limited
    to just dictionary words. 

    EXAMPLE:
    input = Tact Coa
    output = True 
    There exist permutations of the string 'tactcoa' that are palidromes (i.e. 'tacocat')
"""

# Let's begin by thinking of what qualifies a list of values as a palindrome.
# Each value must have a pair exempting one if the length of the list is odd.


def check_palindrome_permute(characters: str) -> bool:
    """Checks if a given string or list is a permutation of a palindrome"""

    characters = characters.replace(" ", "").lower()
    unique_characters = {characters}
    unmatched_char_allowed = len(characters) % 2 != 0

    for character in characters:
        if characters.count(character) % 2 != 0:
            if unmatched_char_allowed:
                unmatched_char_allowed = False
            else:
                return False

    return True
