#!/usr/bin/python3
"""python3 -c print(__import__("square.py").__doc__)
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """python3 -c print(__import__("square.py").Square.__doc__)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """python3 -c print(__import__("square.py").__init__.__doc__)
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """python3 -c print(__import__("square.py").Square.__doc__)
        """
        name = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return f'[{name}] ({id}) {x}/{y} - {size}'
