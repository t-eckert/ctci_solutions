import q4_Is_Palindrome


def test_check_palindrome_permute_with_False_str():
    # given
    test_input = "bananagram"
    expected_result = False

    # when
    actual_result = q4_Is_Palindrome.check_palindrome_permute(test_input)

    # then
    assert expected_result == actual_result


def test_check_palindrome_permute_with_True_str():
    # given
    test_input = "Tact coa"
    expected_result = True

    # when
    actual_result = q4_Is_Palindrome.check_palindrome_permute(test_input)

    # then
    assert expected_result == actual_result


def test_check_palindrome_permute_with_odd_numbered_False_str():
    # given
    test_input = "languid"
    expected_result = False

    # when
    actual_result = q4_Is_Palindrome.check_palindrome_permute(test_input)

    # then
    assert expected_result == actual_result
