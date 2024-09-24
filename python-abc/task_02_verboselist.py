#!/usr/bin/env python3
"""A module that defines a Verboselist class"""


class VerboseList(list):
    """A class that defines a Verboselist class"""

    def append(self, item):
        """A method that appends an item to the list"""
        super().append(item)
        print("Added [{}] to the list".format(item))

    def extend(self, item):
        """A method that extends the list"""
        lenght_item = len(item)
        super().extend(item)
        print("Extended the list with [{}]".format(lenght_item))

    def remove(self, item):
        """A method that removes an item from the list"""
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def pop(self, index=-1):
        """A method that pops an item from the list"""
        item = super().pop(index)
        print("Popped [{}] from the list".format(item))
        return item
