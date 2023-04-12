#!/usr/bin/python3
# 7-add_item.py
"""
Adds all arguments to  Python list, and saves to a  file"""

from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
"""functions imported from task 5 and task 6 respectively"""

item = "add_item.json"

try:
    json_list = load_from_json_file(item)
except FileNotFoundError:
    json_list = []

for arg in argv[1:]:
    json_list.append(arg)

save_to_json_file(json_list, item)
