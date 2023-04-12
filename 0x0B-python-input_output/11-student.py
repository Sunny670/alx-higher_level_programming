#!/usr/bin/python3
# 11-student.py
"""
Contains a class named Student.
"""


class Student:
    """Represents student"""
    def __init__(self, first_name, last_name, age):
        """New student is initialized """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representing  a Student instance
           with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for z in json:
            try:
                setattr(self, z, json[z])
            except FileNotFoundError:
                pass
