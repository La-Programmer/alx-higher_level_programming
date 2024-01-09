#!/usr/bin/python3
"""python3 -c 'print(__import__("3-to_json_string.py").__doc__)'
"""


import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
