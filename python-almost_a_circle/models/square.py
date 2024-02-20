#!/usr/bin/python3
"""importing rectangle for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for the square class."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of the square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the square."""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
