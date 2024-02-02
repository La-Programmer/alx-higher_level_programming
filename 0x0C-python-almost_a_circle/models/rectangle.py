#!/usr/bin/python3
"""python3 -c print(__import__("rectangle.py").__doc__)
"""


from models.base import Base


class Rectangle(Base):
    """python3 -c print(__import__("rectangle.py").Rectangle.__doc__)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """python3 -c print(__import__("rectangle.py").__init__.__doc__)
        """
        super().__init__(id)
        if width.__class__ is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if height.__class__ is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if x.__class__ is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if y.__class__ is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """python3 -c print(__import__("rectangle.py").width.__doc__)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """python3 -c print(__import__("rectangle.py").width.__doc__)
        """
        if value.__class__ is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    @property
    def height(self):
        """python3 -c print(__import__("rectangle.py").height.__doc__)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """python3 -c print(__import__("rectangle.py").height.__doc__)
        """
        if value.__class__ is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.height = value

    @property
    def x(self):
        """python3 -c print(__import__("rectangle.py").x.__doc__)
        """
        return self.__x

    @x.setter
    def x(self, value):
        """python3 -c print(__import__("rectangle.py").x.__doc__)
        """
        if value.__class__ is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.x = value

    @property
    def y(self):
        """python3 -c print(__import__("rectangle.py").y.__doc__)
        """
        return self.__y

    @y.setter
    def y(self, value):
        """python3 -c print(__import__("rectangle.py").y.__doc__)
        """
        if value.__class__ is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.y = value

    def area(self):
        """python3 -c print(__import__("rectangle.py").area.__doc__)
            """
        return self.width * self.height

    def display(self):
        """python3 -c print(__import__("rectangle.py").display.__doc__)
        """
        for i in range(self.y):
            print("")

        for j in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for a in range(self.width):
                print("#", end="")
            print("")
            j += 1

    def __str__(self):
        """python3 -c print(__import__("rectangle.py").__str__.__doc__)
        """
        name = self.__class__.__name__
        id = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return f'[{name}] ({id}) {x}/{y} - {w}/{h}'

    def update(self, *args, **kwargs):
        """python3 -c print(__import__("rectangle.py").update.__doc__)
        """
        attributes1 = ['id', '_Rectangle__width', '_Rectangle__height']
        attributes2 = ['_Rectangle__x', '_Rectangle__y']
        attributes = attributes1 + attributes2
        if len(args) > 0:
            for i in range(min(len(attributes), len(args))):
                if args[i]:
                    setattr(self, attributes[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, key, value)
                else:
                    setattr(self, '_Rectangle__' + key, value)

    def to_dictionary(self):
        """python3 -c print(__import__("rectangle.py").to_dictionary.__doc__)
        """
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}
