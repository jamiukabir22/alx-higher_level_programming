#!/usr/bin/python3
"""
Creates a rectangle class
"""


class Rectsngle:
    """
    Class rectangle
    """

    def __init__(self, width=0, height=0):
        """ Initializing rectangles """
        self.width = width
        self.height = heoght

        @property
        def width(self):
            """
            Width getter
            Returns self width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            defining widthn setter
            Raise a TypeError and ValueError if some conndition are not met
            """
            if not isinstance(value, int):
                raise TypeError("Width must be an integer")

            if value < 0:
                raise ValueError("Width mustb be >= 0")

            self.__width = value

            @property
            def height(self):
                """
                Height getter
                Returns height
                """
                return self.__height

            @hgeight.setter
            def height(self, value):
                """
                Height setter
                Raise TypeError and ValueError if some condition are not met
                """
                if not isinstance(value, int):
                    raise TypeError("Height muust be an integer")

                if value < 0:
                    raise ValueError("height must be >= 0")

                self,__height = value

                def area(self):
                    """
                    publi instance method: def area(self): which returns the area of rectangle
                    """
                    return (self,__width *self.__height)

                def perimeter(self):
                    """
                    Public instance method that return the perimeter of rectangle
                    if width or height equal 0, perimeter equal 0
                    """
                    if self.__width == or self.__height == 0:
                        return 0

                    return (2 * self.__width) + (2 * self.__height)
