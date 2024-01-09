#!/usr/bin/python3
"""python3 -c 'print(__import__("2-append_write.py").__doc__)'
"""


def append_write(filename="", text=""):
    """python3 -c 'print(__import__("2-append_write.py").append_write.__doc__)'
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return myFile.write(text)
