#!/usr/bin/python3
# 4-from_json_string.py
"""
contains  Json to object function
"""
import json


def from_json_string(my_str):
    """returns object represented by JSON string"""
    return json.loads(my_str)
