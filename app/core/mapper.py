""""
MapReduce class

This class is a minimal implementation of
Map Reduce in a sequential approach.
"""


class MapReduce:

    def __init__(self, filename: str, word_list: list):
        self.__filename: str = filename
        self.__word_list: list = word_list
        self.__words_mapped: list = self.mapping()
        self.__words_shuffled: dict = self.shuffle()
        self.__words_reduced: dict = self.reduce()

    def mapping(self) -> list:
        """
        This function iterates the word list and appends to
        list of tuple adding 1 to each word.

        :return A list e.g. [("word1", 1), ("word2", 1]
        """
        return [(x, 1) for x in self.word_list]

    def shuffle(self) -> dict:
        """
        Shuffles a list mapped making word repeated groups.

        :return A dict {"word1":[("word1,1), ("word1",1)]..}
        """
        words_shuffled = dict()
        for line in self.words_mapped:
            if line[0] in words_shuffled:
                words_shuffled[line[0]].append(line)
            else:
                words_shuffled[line[0]] = []
                words_shuffled[line[0]].append(line)
        return words_shuffled

    def reduce(self) -> dict:
        """
        Iterates over the shuffled dictionary and counts
        repeated words. This method is important cause we
        need all words grouped and counted. We still need
        to find in this output dictionary the user input.

        :return A dict e.g. {"word1": 2, "word2": 5}
        """
        words_re = self.words_shuffled.copy()
        for j in self.words_shuffled:
            counter = 0
            for partialCount in self.words_shuffled[j]:
                counter += partialCount[1]
                words_re[j] = counter
        return words_re

    @property
    def words_reduced(self):
        return self.__words_reduced

    @words_reduced.setter
    def words_reduced(self, value):
        self.__words_reduced = value

    @property
    def word_list(self):
        return self.__word_list

    @word_list.setter
    def word_list(self, value):
        self.__word_list = value

    @property
    def filename(self):
        return self.__filename

    @property
    def words_mapped(self):
        return self.__words_mapped

    @words_mapped.setter
    def words_mapped(self, value):
        self.__words_mapped = value

    @property
    def words_shuffled(self):
        return self.__words_shuffled
