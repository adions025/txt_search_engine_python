from core.files import TextFiles

path = '../data/'  # contains some files, please check it
path_dir_empty = '../data/empty/'  # empty folder
file_mng = TextFiles(path)  # object to test


def test_has_files():
    """
    It is assume that path is correct because of args validation.
    Only is tested if contains files or not
    """

    assert file_mng.has_files(path) is True
    assert file_mng.has_files(path_dir_empty) is False


def test_list_files():
    """
    Test list files, only check if there is txt files
    """

    expected_ok = ["../data/adonis1.txt", "../data/adonis2.txt", "../data/empty.txt"]
    expected_fail_no_empty = ["../data/adonis1.txt", "../data/adonis2.txt"]
    expected_fail = ["../data/adonis1.txt", "../data/adonis2.txt", "../data/adonis3.csv"]
    expected_ok_empty = []

    assert file_mng.list_files(path) == expected_ok
    assert not file_mng.list_files(path) == expected_fail
    assert not file_mng.list_files(path) == expected_fail_no_empty
    assert file_mng.list_files(path_dir_empty) == expected_ok_empty


def test_symbols_filters():
    """
    Test to check if symbols filters is working ok.
    In this test was added most common symbols.
    """
    word_result = "hello"
    assert file_mng.symbols_filter("HELLO") == word_result
    assert file_mng.symbols_filter("Hello!") == word_result
    assert file_mng.symbols_filter("hello.") == word_result
    assert file_mng.symbols_filter("¿hello.?") == word_result
    assert file_mng.symbols_filter("¡hello!") == word_result
    assert file_mng.symbols_filter("hello)") == word_result
    assert file_mng.symbols_filter("(hello") == word_result
    assert file_mng.symbols_filter("(hello)") == word_result


def test_extract_file():
    """
    Test to check is a list of word for each txt file
    """

    expected = [["adonis", "test", "hello"], ["adonis", "casa"], []]
    expected_fail = [["adonis", "test", "Hello!"], ["adonis", "casa"]]
    expected_fail_empty = []
    assert not file_mng.extract_file() == expected_fail
    assert not file_mng.extract_file() == expected_fail_empty
    assert file_mng.extract_file() == expected
