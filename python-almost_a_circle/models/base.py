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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
