#!/usr/bin/python3
"""python3 -c 'print(__import__(1-write_file.py).__doc__)'
"""


def write_file(filename="", text=""):
    """python3 -c 'print(__import__("1-write_file.py").write_file.__doc__)'
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
