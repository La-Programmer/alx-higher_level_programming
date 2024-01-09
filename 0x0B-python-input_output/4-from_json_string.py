#!/usr/bin/python3
"""python3 -c 'print(__import__(4-from_json_string.py).__doc__)'
"""


import json


def from_json_string(my_str):
    """python3 -c 'print(__import__("my_module").from_json_string.__doc__)'
    """
    return json.loads(my_str)
