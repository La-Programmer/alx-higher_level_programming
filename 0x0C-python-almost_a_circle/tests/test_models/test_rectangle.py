#!/usr/bin/python3
"""python3 -c print(__import__("test_rectangle.py").__doc__)
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """python3 -c print(__import__("test_rectangle.py").TestRectangle.__doc__)
    """

    @classmethod
    def setUpClass(self):
        """python3 -c print(__import__("test_rectangle.py").setUp.__doc__)
        """
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(12, 10)
        self.r3 = Rectangle(10, 90, 0, 0, 12)

    def test_rectangleId(self):
        """python3 -c print(__import__("test_rectangle").rectangleId.__doc__)
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_rectangleArea(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 120)
        self.assertEqual(self.r3.area(), 900)

    def test_rectangleType(self):
        """python3 -c print(__import__("test_rectangle").rectangleType.__doc__)
        """
        with self.assertRaises(TypeError) as context:
            self.r4 = Rectangle("String", 10, 20, 90)

        exception = context.exception
        self.assertEqual(str(exception), "width must be an integer")

        with self.assertRaises(TypeError) as context:
            self.r4 = Rectangle(20, True, 90, 100)

        exception = context.exception
        self.assertEqual(str(exception), "height must be an integer")

        with self.assertRaises(TypeError) as context:
            self.r4 = Rectangle(20, 30, None, 89)

        exception = context.exception
        self.assertEqual(str(exception), "x must be an integer")

        with self.assertRaises(TypeError) as context:
            self.r4 = Rectangle(40, 50, 80, 100.02902)

        exception = context.exception
        self.assertEqual(str(exception), "y must be an integer")

    def test_rectangleVal(self):
        """python3 -c print(__import__("test_rectangle").rectangleVal.__doc__)
        """
        with self.assertRaises(ValueError) as context:
            self.r5 = Rectangle(0, 10, 20, 90)

        exception = context.exception
        self.assertEqual(str(exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            self.r5 = Rectangle(10, 0, 20, 90)

        exception = context.exception
        self.assertEqual(str(exception), "height must be > 0")

        with self.assertRaises(ValueError) as context:
            self.r5 = Rectangle(70, 10, -20, 90)

        exception = context.exception
        self.assertEqual(str(exception), "x must be >= 0")

        with self.assertRaises(ValueError) as context:
            self.r5 = Rectangle(220, 10, 20, -90)

        exception = context.exception
        self.assertEqual(str(exception), "y must be >= 0")

    @classmethod
    def tearDownClass(self):
        """python3 -c print(__import__("test_rectangle").tearDown.__doc__)
        """
        del self.r1, self.r2, self.r3
