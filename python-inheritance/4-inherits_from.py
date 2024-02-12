#!/bin/usr/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance
of a class that inherited from a_class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
