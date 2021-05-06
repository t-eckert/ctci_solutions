from q4_is_palindrome import check_palindrome_permute

import pytest


@pytest.mark.parametrize(
    "characters,expected",
    [["bananagram", False], ["Tact coa", True], ["languid", False]],
)
def test_check_palidrome_permute(characters, expected):
    # When
    actual = check_palindrome_permute(characters)

    # Then
    assert expected == actual
