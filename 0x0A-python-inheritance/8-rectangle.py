#!/usr/bin/python3
"""
module 8-rectangle
contains BaseGeometry parent class
with public instance method area and integer_validator
contains subclass rectangle
with instantiation of private attribut width and height validated by parent
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherit from BaseGeometry
    Methods:
    __init__(self, width, height)
    """

    def __init__(self, width, height):
        """validate and initialize width and height
        Args:
        width (int): private
        height (int): private
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
