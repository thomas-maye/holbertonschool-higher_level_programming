#!/usr/bin/python3
"""Module for append_write method and returns the number
of characters added."""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8).

    Args:
        filename (str): The file to append.
        text (str): The text to append.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
