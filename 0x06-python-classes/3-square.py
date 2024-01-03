#!/usr/bin/python3
"""python3 -c 'print(__import__("3-square").__doc__)'
"""


class Square:
    """python3 -c 'print(__import__("3-square").Square.__doc__)'
    """
    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        return (self.__size ** 2)
