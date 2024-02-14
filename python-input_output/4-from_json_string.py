#!/usr/bin/python3
"""JSON ovbject (string)"""


def from_json_string(my_str):
    """function that returns the JSON representation of an object (string)"""
    import json
    return json.loads(my_str)
