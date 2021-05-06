from q5_one_away import check_one_away

import pytest


@pytest.mark.parametrize(
    "value_1,value_2,expected",
    [
        ["ple", "pale", True],
        ["Code", "ode", True],
        ["word", "word", True],
        ["hay", "hey", True],
        ["cool", "hot", False],
        ["energy", "matter", False],
        ["a", "abcdefg", False],
    ],
)
def test_check_one_away(value_1, value_2, expected):
    # When
    actual = check_one_away(value_1, value_2)

    # Then
    assert expected == actual
