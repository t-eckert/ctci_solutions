import q1_Is_Unique


def test_are_items_unique_iter_with_unique_str():
    # given
    test_input = "yoke"
    expected_result = True

    # when
    actual_result = q1_Is_Unique.are_items_unique_iter(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_iter_with_not_unique_str():
    # given
    test_input = "bananagram"
    expected_result = False

    # when
    actual_result = q1_Is_Unique.are_items_unique_iter(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_iter_with_unique_list():
    # given
    test_input = [1, 2, 3, 4]
    expected_result = True

    # when
    actual_result = q1_Is_Unique.are_items_unique_iter(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_iter_with_not_unique_list():
    # given
    test_input = [1, 2, 3, 1]
    expected_result = False

    # when
    actual_result = q1_Is_Unique.are_items_unique_iter(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_set_with_unique_str():
    # given
    test_input = "yoke"
    expected_result = True

    # when
    actual_result = q1_Is_Unique.are_items_unique_set(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_set_with_not_unique_str():
    # given
    test_input = "bananagram"
    expected_result = False

    # when
    actual_result = q1_Is_Unique.are_items_unique_set(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_set_with_unique_list():
    # given
    test_input = [1, 2, 3, 4]
    expected_result = True

    # when
    actual_result = q1_Is_Unique.are_items_unique_set(test_input)

    # then
    assert expected_result == actual_result


def test_are_items_unique_set_with_not_unique_list():
    # given
    test_input = [1, 2, 3, 1]
    expected_result = False

    # when
    actual_result = q1_Is_Unique.are_items_unique_set(test_input)

    # then
    assert expected_result == actual_result

