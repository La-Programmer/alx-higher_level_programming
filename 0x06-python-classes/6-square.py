#!/usr/bin/python3
"""python3 -c 'print(__import__("6-square").__doc__)'
"""


class Square:
    """python3 -c 'print(__import__("6-square").Square.__doc__)'
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        if isinstance(position, tuple) and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """python3 -c 'print(__import__("6-square").size.__doc__)'
        """
        return self.__size

    @property
    def position(self):
        """python3 -c 'print(__import__("6-square").position.__doc__)'
        """
        return self.__position

    @size.setter
    def size(self, value):
        """python3 -c 'print(__import__("6-square").size.__doc__)'
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """python3 -c 'print(__import__("6-square").position.__doc__)'
        """
        if isinstance(value, tuple) and len(value) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """python3 -c 'print(__import__("6-square").area.__doc__)'
        """
        return self.__size ** 2

    def my_print(self):
        """python3 -c 'print(__import__("6-square").my_print.__doc__)'
        """
        y = 0
        i = 0
        while (y < self.__position[1]):
            print("")
            y += 1
        while (i < self.__size):
            j = 0
            x = 0
            while (x < self.__position[0]):
                print(" ", end="")
                x += 1
            while (j < self.__size):
                print("#", end="")
                j += 1
            print("")
            i += 1
        if (self.__size == 0):
            print("")
