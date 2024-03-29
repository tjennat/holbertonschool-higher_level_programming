#!/usr/bin/python3
"""empty class that defines a square."""


class Square:
    """empty class that defines a square."""

    __size = None

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
