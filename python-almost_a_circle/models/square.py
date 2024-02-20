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
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value
