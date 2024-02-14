#!/usr/bin/python3
"""Reads a text file and prints number of char"""


def write_file(filename="", text=""):
    """Write a function that writes a string to a text file and
returns the number of characters written"""
    with open(filename, "w") as f:
        return f.write(text)
