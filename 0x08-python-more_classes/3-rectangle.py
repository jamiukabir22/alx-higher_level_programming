#!/usr/bin/python3
"""
Creates a rectangle class
"""

class Rectangle:
    """
    rectangle class
    """

    def __int__(self, width=0, height=0):
        """ Initialise rectangles """
        self.width = width
        self.height = height

        @property
        def width(self):
            """
            width getter
            Returns self width
            """
            return self.__width

        @width.setter
        def width(self, value):
            """
            defines the width setter
            Raise TypeError and ValueError if some conditions are met
            """
            if not isinstance(vlaue, int):
                raise TypeError("width must be an integer")

            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

            @property
            def height(self):
                """
                Height getter
                Returns height
                """
                return seld.__height

            @height.setter
            def height(self, value):
                """
                Height setter
                Raise TypeError and ValueError if some cnditions are met
                """
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")

                if value < 0:
                    raise ValueError("height must be >= 0")

                self.__height = value

                def area(self):
                    """
                    Public instance method: def area(self): returns the area rectangle
                    """
                    return (self.__width * self.__height)

                def perimeter(self):
                    """
                    Public instance method which returns the rectangle perimeter
                    if width or height equals 0, perimeter equa;s 0
                    """
                    if self.__width == 0 or self.__height == 0:
                        return 0

                    return ( * self.__width) + (2 * self.__height)
                
                def __str__(self):
                    """
                    print() and str() should print a rectangle with the character #
                    """
                    if self.__width = 0 or self.__heght == 0:
                        return""

                    st = "\n".join(["#" * self.__width for rows in range(self.__height)])
                    return st

