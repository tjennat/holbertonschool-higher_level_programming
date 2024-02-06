#!/usr/bin/python3
"""empty class that defines a square."""


class Square:
    """empty class that defines a square."""

    size = None

    def __init__(self, size):
        if isinstance(size, int):
            self.size = size
        else:
            return None
