#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A class that inherits from list."""

    def print_sorted(self):
        """Print a sorted list."""
        print(sorted(self))
