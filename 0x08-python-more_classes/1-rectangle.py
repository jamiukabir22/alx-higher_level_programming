#!/usr/bin/python3
"""
Creates a rctangle class
"""


class Rectangle:
    """
    the class rectangle
    """

    def __int__(self, width=0, height=0):
        """ Initializing rectangle """
        sel.width = width
        self.height =height

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
            defining width setter
            Raise a TypeError and ValueError if some conditions not met
            """
            if not isintance(value, int):
                raise TypeError("Width must be an integer")

            if value < 0:
                raise ValueError("Width must be >= 0")

            self.__width = value

            @property
            def height(self):
                """
                Height setter
                Returns height
                """
                return self,__height

            @height.setter
            def height(self, value):
                """
                Height setter
                Raise a TypeError and Value Error if come conditions not met
                """
                if not isintsance(value, int):
                    raise TypeError("Height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")

                self.__height = value
