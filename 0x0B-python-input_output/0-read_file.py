#!/usr/bin/python3
"""python3 -c 'print(__import__("0-read_file.py").__doc__)'
"""


def read_file(filename=""):
    """python3 -c 'print(__import__("0-read_file.py").read_file.__doc__)'
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        while True:
            result = myFile.readline()
            if result:
                print(result, end="")
            else:
                break
