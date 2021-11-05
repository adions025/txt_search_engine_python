from core.mapper import MapReduce
from main import find_results


def test_find_results():
    # Filenames
    filename = 'adonis1.txt'
    filename_two = 'adonis2.txt'

    # Word files
    word_list = ["adonis", "hello", "test"]
    words_duplicated = ["adonis", "adonis"]

    # MapReduce objects
    map_obj = MapReduce(filename, word_list)
    map_obj_duplicated = MapReduce(filename_two, words_duplicated)

    # Because the function receive a list of MapReduce objects
    map_one = [map_obj]
    map_two = [map_obj_duplicated]
    # Using two files to find results
    map_three = [map_obj, map_obj_duplicated]

    # User input word list examples (list format)
    word = ["adonis"]
    no_in = ["house"]
    two_words = ["adonis", "test"]
    two_word_one_mno = ["adonis", "house"]
    three_word = ["adonis", "hello", "test"]
    empty_word = []

    assert find_results(map_one, word) == [('adonis1.txt', 100.0, 101.0)]
    assert find_results(map_one, no_in) == [('adonis1.txt', 0.0, 0.0)]
    assert find_results(map_one, two_words) == [('adonis1.txt', 100.0, 102.0)]
    assert find_results(map_one, two_word_one_mno) == [('adonis1.txt', 50.0, 51.0)]
    assert find_results(map_one, three_word) == [('adonis1.txt', 100.0, 103.0)]
    assert find_results(map_one, empty_word) == []

    assert find_results(map_two, word) == [('adonis2.txt', 100.0, 102.0)]
    assert find_results(map_two, no_in) == [('adonis2.txt', 0.0, 0.0)]
    assert find_results(map_two, two_words) == [('adonis2.txt', 50.0, 52.0)]
    assert find_results(map_two, two_word_one_mno) == [('adonis2.txt', 50.0, 52.0)]
    assert find_results(map_two, three_word) == [('adonis2.txt', 33.0, 35.0)]
    assert find_results(map_two, empty_word) == []

    assert find_results(map_three, word) == [('adonis1.txt', 100.0, 101.0), ('adonis2.txt', 100.0, 102.0)]
    assert find_results(map_three, no_in) == [('adonis1.txt', 0.0, 0.0), ('adonis2.txt', 0.0, 0.0)]
    assert find_results(map_three, two_words) == [('adonis1.txt', 100.0, 102.0), ('adonis2.txt', 50.0, 52.0)]
    assert find_results(map_three, two_word_one_mno) == [('adonis1.txt', 50.0, 51.0), ('adonis2.txt', 50.0, 52.0)]
    assert find_results(map_three, three_word) == [('adonis1.txt', 100.0, 103.0), ('adonis2.txt', 33.0, 35.0)]
    assert find_results(map_three, empty_word) == []

    assert find_results(map_three, three_word) == [('adonis1.txt', 100.0, 103.0), ('adonis2.txt', 33.0, 35.0)]
    assert find_results(map_three, three_word) == [('adonis1.txt', 100.0, 103.0), ('adonis2.txt', 33.0, 35.0)]

    assert find_results(map_three, empty_word) == []
    assert find_results(None, word) == []
    assert find_results(None, empty_word) == []
