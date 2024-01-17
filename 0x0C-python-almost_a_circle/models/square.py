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

    @property
    def size(self):
        """python3 -c print(__import__("rectangle.py").width.__doc__)
        """
        return self.width

    @size.setter
    def size(self, value):
        """python3 -c print(__import__("rectangle.py").width.__doc__)
        """
        if value.__class__ is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """python3 -c print(__import__("rectangle.py").update.__doc__)
        """
        attributes = ["id", "size", "x", "y"]
        if len(args) > 0:
            for i in range(min(len(attributes), len(args))):
                if args[i]:
                    if attributes[i] == "size":
                        self.width = args[i]
                        self.height = args[i]
                    else:
                        setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
