"""
Settings class

Some settings parameters.
"""

import os


class Settings:
    PROJECT_NAME: str = "Text search engine"

    ROOT_DIR = os.path.abspath("../")
    DEFAULT_PATH_FILE = os.path.join(ROOT_DIR, "data")

    FILE_EXT = ".txt"
    TOP_RANKED = 10


settings = Settings()
