#!/usr/bin/python3
"""
Contains "class_to_json" function
"""


def class_to_json(obj):
    """returns a dictionary description with simple data structure
      (string, integer, list, dictionary and boolean)
      for JSON serialization of an object"""
    return obj.__dict__