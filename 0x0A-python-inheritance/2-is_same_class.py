#!/usr/bin/python3
"""python3 -c 'print(__import__("2-is_same_class.py").__doc__)'
"""


def is_same_class(obj, a_class):
    """python3 -c 'print(__import__("my_module").is_same_class.__doc__)'
    """
    if type(obj) is a_class:
        return True
    return False
