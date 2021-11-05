from core.util import *


def test_sum_dictionary():
    """
    Test to validate the result of sum dictionary
    """
    test = {"house": 1}
    test_1 = {"house": 1, "family": 5}
    test_2 = {"house": 1, "family": 5, "horse": 4}
    test_empty = {}
    assert sum_dictionary(test) == 1
    assert sum_dictionary(test_1) == 6
    assert sum_dictionary(test_2) == 10
    assert sum_dictionary(test_empty) == 0
    assert sum_dictionary(None) == 0


def test_calculate_percentage():
    """
    Test to validate the correct result of percentage
    """
    # (corrects words found, total words to search)
    assert calculate_percentage(4, 4) == 100
    assert calculate_percentage(2, 4) == 50
    assert calculate_percentage(3, 4) == 75
    assert calculate_percentage(1, 4) == 25
    assert calculate_percentage(0, 4) == 0
    assert calculate_percentage(0, 0) == 0  # 0 division


def test_find_unique_elements():
    """
    Test to validate the find unique elements functions.
    """
    words = ["house", "house", "adonis"]
    expected_word = ["house", "adonis"]

    words_2 = ["key", "pen"]
    expected_word_2 = ["key", "pen"]

    words_3 = []
    expected_word_3 = []

    assert find_unique_elements(words) == expected_word
    assert find_unique_elements(words_2) == expected_word_2
    assert find_unique_elements(words_3) == expected_word_3
