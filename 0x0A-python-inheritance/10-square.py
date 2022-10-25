#!/usr/bin/python3
"""
Contains BaseGeometry parent class
with public instance method area and integer-VALIDATOR
contains subclass Rectangle
contains subclass Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle, who inherits for BaseGeometry
    Methods:
    __init__(self, size)
    """

    def __init__(self, size):
        """Initailse size
        Args:
        size (int): private
        """
        self.__integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
