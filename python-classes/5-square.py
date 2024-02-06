#!/usr/bin/python3
"""empty class that defines a square."""


class Square:
    """empty class that defines a square."""

    __size = None

    @property
    def size(self):
        return self.__size

    def __init__(self, __size=0):
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size

    def area(self):
        """returns the current square area"""

        return self.__size * self.__size

    @size.setter
    def size(self, value):
        """getter function for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
