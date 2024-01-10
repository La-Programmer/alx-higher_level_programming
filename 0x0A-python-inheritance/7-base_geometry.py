#!/usr/bin/python3
"""python3 -c 'print(__import__("7-base_geometry.py").__doc__)'
"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").BaseGeometry.__doc__)'
    """
    def area(self):
        """python3 -c 'print(__import__("my_module").class.function.__doc__)'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """python3 -c 'print(__import__("my_module").class.function.__doc__)'
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
