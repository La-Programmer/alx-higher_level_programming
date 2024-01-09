#!/usr/bin/python3
"""python3 -c 'print(__import__("5-save_to_json_file.py").__doc__)'
"""


import json
import os


def save_to_json_file(my_obj, filename):
    """python3 -c 'print(__import__("my_module").save_to_json_file.__doc__)'
    """
    my_str = json.dumps(my_obj)

    with open(filename, mode="w", encoding="utf-8") as myfile:
        myfile.write(my_str)
