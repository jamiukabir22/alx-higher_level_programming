#!/usr/bin/python3
"""
An empty class
"""

class BaseGeometry:
    """public instance method: def area(self)"""

    def area(self):
        """raise an exception with message area () is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
