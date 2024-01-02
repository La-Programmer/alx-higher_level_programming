#!/usr/bin/python3
class Square:
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width

    @staticmethod
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    @property
    def height(self):
        print("Retrieving the height")
        return self.__height

    @height.setter
    def height(self, value):
        if self.isfloat(value):
            self.__height = value
        else:
            print("Please only enter a number")

    @property
    def width(self):
        print("Retrieving the width")
        return self.__width

    @width.setter
    def width(self, value):
        if self.isfloat(value):
            self.__width = value
        else:
            print("Please only enter a number")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    sq1 = Square()

    height = input("Enter Height: ")
    width = input("Enter Width: ")

    sq1.height = height
    sq1.width = width

    print("Height: {}".format(sq1.height))
    print("Width: {}".format(sq1.width))
    print("The Area is: ", sq1.getArea())


if __name__ == "__main__":
    main()
