#!/usr/bin/python3
"""python3 -c 'print(__import__("6-load_from_json_file.py").__doc__)'
"""


import json


def load_from_json_file(filename):
    """python3 -c 'print(__import__("my_module").load_from_json.__doc__)'
    """
    with open(filename, mode="r", encoding="utf-8") as myFile:
        json_str = myFile.read()
    return json.loads(json_str)
