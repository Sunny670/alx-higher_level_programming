#!/usr/bin/python3
# 10-student.py
"""Contains a class named  Student."""


class Student:
    """Represents student."""

    def __init__(self, first_name, last_name, age):
        """New Student is initialized .
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary representing the Student.
        If attrs is list of strings, represents only attributes that are
        included in the list.
        Args:
            attrs (list): Attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__