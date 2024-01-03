#!/usr/bin/python3
"""python3 -c 'print(__import__("5-square").__doc__)'
"""


class Square:
    """python3 -c 'print(__import__("5-square").Square.__doc__)'
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """python3 -c 'print(__import__("5-square").size.__doc__)'
        """
        return size.__self

    @size.setter
    def size(self, value):
        """python3 -c 'print(__import__("5-square").size.__doc__)'
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """python3 -c 'print(__import__("5-square").area.__doc__)'
        """
        return (self.__size ** 2)

    def my_print(self):
        i = 0
        j = 0
        while (i < self.__size):
            j = 0
            while (j < self.__size):
                print("#", end="")
                j += 1
            print("")
            i += 1
        if (self.__size == 0):
            print("")
