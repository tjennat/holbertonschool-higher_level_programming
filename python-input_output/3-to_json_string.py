#!/usr/bin/python3
"""JSON ovbject (string)"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    import json
    obj = my_obj
    return json.dumps(obj)
