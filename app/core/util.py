"""
Util functions
"""


def sum_dictionary(dictionary: dict) -> int:
    """
    Receive a dictionary and return the total values sum.

    :param dictionary: {"house":1}
    :return: A int, sum of values
    """
    if dictionary is None:
        return 0
    return sum([dictionary[j] for j in dictionary])


def calculate_percentage(words_ok: int, num_words: int) -> int:
    """
    This is the formula to calculate the percentage.


    :param words_ok: A int,  correct words in a file
    :param num_words: A int,  words introduced by user
    :return: A int, the result of operation
    """
    if num_words == 0:
        return 0
    return int(words_ok * 100 / num_words)


def find_unique_elements(phrases: list) -> list:
    """
    To remove repeated elements from a list.

    :param phrases: A list of strings
    :return: A list without repeated elements
    """
    seen = set()
    return [x for x in phrases if x not in seen and (seen.add(x) or True)]
