#!/usr/bin/python3
"""Module for write_file method."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8).

    Args:
        filename (str): The file to write.
        text (str): The text to write.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
