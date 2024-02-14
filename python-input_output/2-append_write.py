#!/usr/bin/python3
"""Reads a text file and prints number of char"""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text file
and returns the number of characters added:"""
    with open(filename, "a") as f:
        return f.write(text)
