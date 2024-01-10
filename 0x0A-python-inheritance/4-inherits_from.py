#!/usr/bin/python3
"""python3 -c 'print(__import__("4-inherits_from.py").__doc__)'
"""


def inherits_from(obj, a_class):
    """python3 -c 'print(__import__("4-inherits").inherits_from.__doc__)'
    """
    if issubclass(type(obj), a_class):
        return True
    return False
