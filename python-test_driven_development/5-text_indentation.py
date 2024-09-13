#!/usr/bin/python3
""" Module for text_indentation method """


def text_indentation(text):
    """ Method to print a text with 2 new lines after each of
    these characters: ., ? and :

    Args:
        text: text to be printed

    Raises:
        TypeError: if text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
