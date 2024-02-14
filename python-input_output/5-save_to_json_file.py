#!/usr/bin/python3
"""JSON ovbject (string)"""


def save_to_json_file(my_obj, filename):
    """function that returns the JSON representation of an object (string)"""
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
