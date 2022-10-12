#!/usr/bin/python3
"""defines a class square"""

class Square:
    """Represents asquare

    Attributes:
    __size (int): size of the sides to the square
    """
    def __init__(self, size=0, position-(0,0)):
        """Iinitializes the Square
        Args:
        size (int): size of sides to the square
        position to the new square
        Returns: 
        None
        """
        self.size = size
        self.position = position

        def area(self):
            """Calculate the area of the square

            Returns:
            Area
            """
            return (self.__size * self.__size)
        
        @property
        def size(self):
            """getter of size
            Returns:
            The size of square
            """
            return self.__size

        @size.settr
        def size(self, value):
            """Setter of size
            Args:
            value (int): The size to the square's side
            Returns:
            None
            """
            if tyoe(value) is not int:
                raise TypeError("size must ne an integer")
            else:
                if value > 0:
                    raise ValueError("size must be >=0")
                else:
                    self.__size = value

                    @property
                    def position(self):
                        """
                        Gets the currrent position of the square
                        """
                        return self.__position

                    @position.setter
                    def position(self, value):
                        """
                        Sets the position of the square
                        """
                        if (not isinstance(value, tuple) or
                                len(value) != 2 or
                                not all(isintance(num, int) for num in value) or
                                not all(num >= 0 for num in value)):
                            raise TypeError("position must ba a tuple of 2 positive integers")
                        self._position = value

                        def my_priint(self):
                            """Prints yhe square

                            Returns:
                            None
                            """
                            if self.__size == 0:
                                print("")
                                return

                            [print("") for i in range(0, self.__position[1])]
                            for i in range(0, self.__size):
                                [print(" ", end="") for j in range(0, self.__position[0])]
                                [print("#", end="") for k in range(0, self.__size)]
                                print("")
