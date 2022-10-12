#!/usr/bin/python3
"""define a class square"""


class Square:
    """Represents a square


    Attributes:
    __size (int): size of the sides of a square
    """
    def __init__(self, size=0):
        """Initializes the square
        Args:
        size (int): size of tthe sides os square
        Returns:
        Noone
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >=")
            else:
                self.__size = size
