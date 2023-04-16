#!/usr/bin/python3
"""
Contains a "Square" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """New Square initialized.
        Args:
            size (int): size of new Square.
            x (int): x coordinate of new Square.
            y (int): y coordinate of new Square.
            id (int): identity of new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the Square.
        Args:
            *args (ints): New attribute values.
                - 1st arg represents the id attribute
                - 2nd arg represents the size attribute
                - 3rd arg represents the x attribute
                - 4th arg represents the y attribute
            **kwargs (dict): New value pair of attributes.
        """
        if args and len(args) != 0:
            z = 0
            for arg in args:
                if z == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif z == 1:
                    self.size = arg
                elif z == 2:
                    self.x = arg
                elif z == 3:
                    self.y = arg
                z += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """Returns a dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns print() and str() representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
