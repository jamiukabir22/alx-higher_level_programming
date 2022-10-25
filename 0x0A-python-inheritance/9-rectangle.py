#!/usr/bin/python3
"""
Task 9
Contains BaseGeometry parent class
with public instance method area and integer_validator
contains a subclass Rectangle
with instantiatin ofprivate attribute width and height validatwd by parennt,
extends parent's area method ND PRINTS WITH _str__
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectanglw(BaseGeometry):
    """Inhetrits from BaseGrometry
    Methode:
    __init__(self, width, height)
    area(self)
    __str__
    """

    def __init__(self, width, height):
        """validation and initialization of width and height
        Args:
        width (int): private
        height (int): private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

        def area(self):
            """extends parents empty method and returns area"""
            return self.__width * self.__height

        def __str__(self):
            """prints [rectangle] <width>/<height>"""
            return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,self.__width, self.__height)
