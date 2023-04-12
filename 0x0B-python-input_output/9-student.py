#!/usr/bin/python3
# 9-student.py
"""
Contains a class named "Student"
"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """New student is initialized"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary that represents a Student instance"""
        return self.__dict__
