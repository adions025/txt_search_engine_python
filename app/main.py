"""
Text search engine

@author: Adonis Gonzalez
"""
from core.files import TextFiles
from core.config import settings
from os.path import exists, isdir
from core.mapper import *
from core.util import *
import argparse


def find_results(map_files: list, search: list) -> list:
    """
    Iterates over reduced words to find the user input words.
    Results are returned as a list of tuples.

    :param map_files: A list of MapReduce objs (each file)
    :param search:  A list of word to search
    :return: A list of final results
    """
    if not search or not map_files:
        return []

    result_final = []
    results = dict()
    for m in map_files:
        found = dict()
        for i, j in m.words_reduced.items():
            [found.update({x: j}) for x in search if str(x).lower() == i]
        results.update({m.filename: found})

    for j, x in results.items():
        total = calculate_percentage(len(x), len(search))
        result_final.append((j, total, total + sum_dictionary(x)))
    return result_final


def print_results(results: list):
    """
    Function to print results, also a list of tuple is sorted.
    If first element is 0 then not matches found,
    if iterator is bigger than ranked then break.

    :param results: A list of 3d-tuples (filename, percent, betaPercent)
    :print results > filename:100%
    """
    if results:
        results.sort(key=lambda j: j[2], reverse=True)
        for j, i in enumerate(results):
            if j == 0 and results[j][1] == 0:
                print("not matches found")
                break
            if j < settings.TOP_RANKED:
                if results[j][1] > 0:
                    print("%s : %d%s" % (results[j][0], results[j][1], "%"))
            else:
                break


def parse_args():
    """
    The function will parse arguments. These arguments will be
    defined by the user on the console.

    :return: args
    """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description=settings.PROJECT_NAME)
    parser.add_argument("command",
                        metavar="<command>",
                        help="'search'")
    parser.add_argument('--path', required=True,
                        # default=settings.DEFAULT_PATH_FILE,
                        metavar="/path/to/",
                        help="Path to files'")
    args = parser.parse_args()

    # Validate arguments
    if args.command == "search":
        assert args.path, "Argument --path is required"
    if args.path:
        assert exists(args.path), "--path is not correct"
        assert isdir(args.path), "--path must be a dir not a file"
    return args


if __name__ == "__main__":
    """
    Start program
    """

    args = parse_args()
    files_mng = TextFiles(args.path)
    maps = [MapReduce(x, files_mng.words[i]) for i, x in enumerate(files_mng.files)]

    phrase = ''
    while phrase != "quit":
        phrase = input("search > ").split()
        if phrase:
            if phrase[0] == "quit":
                break
        else:
            continue

        phrase = find_unique_elements(phrase)
        final_results = find_results(maps, phrase)
        print_results(final_results)
