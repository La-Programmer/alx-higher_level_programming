#!/usr/bin/python3
def add_integer(a, b=98):
    """print(__import__("0-add_integer").__doc__)
    """

    type_arr = [int, float]
    if type(a) not in type_arr:
        raise TypeError("a must be an integer")
    if type(b) not in type_arr:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
