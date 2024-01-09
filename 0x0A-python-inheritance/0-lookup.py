#!/usr/bin/python3
"""python3 -c 'print(__import__("0-lookup.py").__doc__)'
"""


def lookup(obj):
    """python3 -c 'print(__import__("0-lookup.py").lookup.__doc__)'
    """
    return dir(obj)
