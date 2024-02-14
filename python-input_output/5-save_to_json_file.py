#!/usr/bin/python3
"""JSON ovbject (string)"""


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    import json
    with open(filename, 'w'):
        return json.dump(my_obj, filename)
