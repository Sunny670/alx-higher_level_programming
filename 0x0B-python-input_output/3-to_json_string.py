#!/usr/bin/python3
# 3-to_json_string.py
"""
contains a string to JSON module
"""
import json


def to_json_string(my_obj):
    """returns JSON representation of  object (string)"""
    return json.dumps(my_obj)
