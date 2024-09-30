#!/usr/bin/python3
"""Module for read_file method."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The file to read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
