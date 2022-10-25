#!/usr/bin/python3
"""
Task 10
Contains BaseGeometry parent class
subclass Rectangle
subclass square
"""
Rectangle = __import__('9-rectangle'0.Rectangle


        class Square(Rectangle):
        """Inherits from Rectangle, who inherits from BaseGeometry
        Methods:
        __init__(self, size)
        """

        def __init__(self, size):
        """Initailize size
        Args:
        size (int): private
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
