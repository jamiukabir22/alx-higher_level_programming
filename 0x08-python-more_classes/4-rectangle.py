#!/usr/bin/python3
"""
Creates a rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """ Initailize rectangles """
        self.width = width
        self.height = height

        @property
        def width(self):
            """"
            Width getter
            Returns self width
            """
            return self._width

        @width.setter
        def width(self, value):
            """
            defines the width setter
            Raise TypeError and ValueError if some condition can be met
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")

            if value < 0:
                raise VlueError("width must be >= 0")

            self.__width = value

            @property
            def height(self):
                """
                height getter
                Returns height
                """
                return self.__height

            @height.setter
            def height(self, value):
                """
                Height setter
                Raise TypeError and ValueError if some condition can not be met
                """
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")

                if value <0:
                    raise ValueError("height must be >= 0")

                self.__height = value

                def area(self):
                    """
                    Public instance method: def area(self): returns area of rectangle
                    """
                    return (self.__height * self.__width)

                def perimeter(self):
                    """
                    Public instance method return perimeter of rectangle
                    if width or height equals 0, perimeter equals 09
                    """
                    if self.__width == 0 or self.__height == 0:
                        return 0

                    return (2 * self.__width) + (*2 * self.__height)

                def __str__(self):
                    """
                    print() and str() prints the rectangle with the character #
                    """
                    if self.__width == 0 or self.__height == 0:
                        return ""

                    st = "\n".join(["#" * self.__width for rows in range(self.__height)])
                    return st

                def __repr__(self):
                    """
                    Returns a string representation of teh rectangle
                    recreayes a new instnce
                    """
                    return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
