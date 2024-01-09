#!/usr/bin/python3
"""python3 -c 'print(__import__("7-add_item.py").__doc__)'
"""


import sys
import os
import json


save_to = __import__('5-save_to_json_file').save_to_json_file
load_from = __import__('6-load_from_json_file').load_from_json_file
list = []
filename = "add_item.json"
if os.path.exists(filename):
    list = load_from(filename)
counter = 1
while counter < len(sys.argv):
    list.append(sys.argv[counter])
    counter += 1
buffer = json.dumps(list)
save_to(list, filename)
