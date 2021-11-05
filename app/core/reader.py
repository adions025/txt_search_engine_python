"""
A helper class that has ABCMeta as its metaclass.
With this class, an interface base class can be
created.
"""

from abc import abstractmethod
from abc import ABCMeta


class IReader(metaclass=ABCMeta):

    @abstractmethod
    def has_files(self):
        pass

    @abstractmethod
    def list_files(self):
        pass

    @abstractmethod
    def extract_file(self):
        pass
