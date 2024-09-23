#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A class MyList that inherits from the list"""
    def __init__(self):
        """Initializes the MyList object"""
        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)"""
        print(sorted(self))
