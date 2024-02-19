#!/usr/bin/python3
"""
class that will be the base"""


class Base:
    """this class is going to be the base of the project"""
    __nb_objects = 0


    def __init__(self, id=None):
        """is the class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
