#!/usr/bin/python3
"""python3 -c 'print(__import__("base.py").__doc__)'
"""


class Base:
    """python3 -c 'print(__import__("base.py").Base.__doc__)'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """python3 -c 'print(__import__("base.py").Base.__init__.__doc__)'
        """
        if id:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
