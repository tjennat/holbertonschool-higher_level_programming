#!/usr/bin/python3
"""
This is the "4-print_square" module.


"""


def print_square(size):
    """
    print square of size n
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
