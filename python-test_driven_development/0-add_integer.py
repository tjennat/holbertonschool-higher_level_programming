#!/usr/bin/python3
"""This module defines the add_integer function



"""


def add_integer(a, b=98):
    """This function adds two integers
    sum of two integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a+b)
