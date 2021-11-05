from core.mapper import MapReduce

filename = 'adonis1.txt'

word_list = ["adonis", "hello", "test"]
words_duplicated = ["adonis", "adonis"]

map_obj = MapReduce(filename, word_list)
map_obj_duplicated = MapReduce(filename, words_duplicated)


def test_mapping():
    """
    Test to check mapping function, should return a list of tuple,
    for each word a 1 added.
    """

    assert map_obj.mapping() == [("adonis", 1), ("hello", 1), ("test", 1)]
    assert not map_obj.mapping() == [{"adonis", 1, "hello", 1, "test", 1}]
    assert map_obj_duplicated.mapping() == [("adonis", 1), ("adonis", 1)]
    assert not map_obj_duplicated.mapping() == [("adonis", 2)]
    assert not map_obj_duplicated.mapping() == [{"adonis", 1}]


def test_shuffle():
    """
    Test to check shuffle function
    """

    assert map_obj.shuffle() == {'adonis': [('adonis', 1)], 'test': [('test', 1)], 'hello': [('hello', 1)]}
    assert not map_obj.shuffle() == [("adonis", 1), ("hello", 1), ("test", 1)]
    assert not map_obj.shuffle() == [{"adonis", 1, "hello", 1, "test", 1}]
    assert map_obj_duplicated.shuffle() == {'adonis': [('adonis', 1), ('adonis', 1)]}
    assert not map_obj_duplicated.shuffle() == [("adonis", 2)]
    assert not map_obj_duplicated.shuffle() == {'adonis': 2}


def test_reduce():
    """
    Test to check reduce function
    """
    assert map_obj.reduce() == {'adonis': 1, 'test': 1, 'hello': 1}
    assert map_obj_duplicated.reduce() == {'adonis': 2}
