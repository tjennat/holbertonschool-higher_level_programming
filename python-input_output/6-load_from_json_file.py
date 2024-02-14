#!/usr/bin/python3
"""JSON object from JSON file"""


def load_from_json_file(my_obj, filename):
    """function that creates an object from a JSON file"""
    import json
    with open(filename, "r") as file:
        return json.load(file)
