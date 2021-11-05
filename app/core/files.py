"""
TextFiles class

Manage files from a given path and
splits them by words.
Contains a word list for each file.
"""

from core.config import settings
from core.reader import *
from os.path import join
from os import listdir


class TextFiles(IReader):
    def __init__(self, path: str):
        # Check if there is any files in the given path to continue
        if not self.has_files(path):
            print("Not file found, try using other path or adding files")
            exit(0)  # Exit cause atm path only can be set by args
        self.__files: list = self.list_files(path)
        self.__words: list = self.extract_file()

    def extract_file(self) -> list:
        """
        This method reads words from each file and appends to a list.

        :return A list of words for each file
        """
        file_words = [(open(j, errors="ignore").read().split()) for j in self.files]
        return [[self.symbols_filter(j) for j in w] for w in file_words]

    @staticmethod
    def has_files(path: str) -> bool:
        """
        Checks if there is any file in the given path.
        If not files, is not possible continue.

        :param path: A str like /to/path/
        :return: A bool True/False
        """
        return any([j for j in listdir(path) if j.endswith(settings.FILE_EXT)])

    @staticmethod
    def list_files(path: str) -> list:
        """
        Return a list of files that ends with .txt extension

        :param path: A str like /to/path/
        :return: A list that contains all found files
        """
        return [(join(path, j)) for j in listdir(path) if j.endswith(settings.FILE_EXT)]

    @staticmethod
    def symbols_filter(word: str) -> str:
        """
        This method remove all the symbols, and also change
        each word to lowercase.

        :param word: A str "word1"
        :return: A str, same word received without symbols
        """
        return ''.join([j for j in word if not (j in ';-¿?.,¡!:()')]).lower()

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, value):
        self.__words = value

    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, value):
        self.__files = value
