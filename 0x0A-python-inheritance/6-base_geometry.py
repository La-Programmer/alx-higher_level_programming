#!/usr/bin/python3
"""python3 -c 'print(_import__("6-base_geometry.py").__doc__)'
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
