#!/usr/bin/python3
"""Module for Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Class that represents a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for the Rectangle class with width and height"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
