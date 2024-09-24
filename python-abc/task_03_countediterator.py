#!/usr/bin/env python3
"""A module that defines keeping track of the number of iterations"""


class CountedIterator:
    """A class that defines keeping track of the number of iterations"""

    def __init__(self, iterable, count=0):
        """A method that initializes the class"""
        self.count = count
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        """
        A method that returns the iterator object

        Returns:
            self: the iterator object
        """
        return self

    def __next__(self):
        """
        A method that returns the next item in the iteration

        Returns:
            self.iterable[self.index - 1]: the next item in the iteration

        Raises:
            StopIteration: when the iteration is done
        """
        if self.index < len(self.iterable):
            self.index += 1
            self.count += 1
            return self.iterable[self.index - 1]
        else:
            raise StopIteration

    def get_count(self):
        """
        A method that returns the number of iterations

        Returns:
            self.index: the number of iterations
        """
        return self.index
