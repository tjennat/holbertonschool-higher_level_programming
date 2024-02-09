#!/usr/bin/python3
""""This is '5-text_indentation' module
"""


def text_indentation(text):
    """"
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in ('.', '?', ':'):
            print('\n')
