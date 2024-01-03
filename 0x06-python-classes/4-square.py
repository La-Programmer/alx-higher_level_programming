#!/usr/bin/python3
"""python3 -c 'print(__import__("4-square").__doc__)'
"""


class Square:
    """python3 -c 'print(__import__("4-square").Square.__doc__)'
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """python3 -c 'print(__import__("4-square").square.__doc__)'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """python3 -c 'print(__import__("4-square").square.__doc__)'
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """python3 -c 'print(__import__("4-square").area.__doc__)'
        """
        return (self.__size ** 2)
