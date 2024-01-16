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
        self.r3 = Rectangle(10, 90, 845, 395, 12)
        self.r6 = Rectangle(12, 13, 8)
        self.r7 = Rectangle(98, 99, 100)
        self.r8 = Rectangle(81, 9, 11)

    def test_rectangleId(self):
        """python3 -c print(__import__("test_rectangle").rectangleId.__doc__)
        """
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)

    def test_rectangleArea(self):
        """python3 -c print(__import__("test_rectangle").rectangleArea.__doc__)
        """
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

    def test_Display(self):
        """python3 -c print(__import__("test_rectangle.py").Display.__doc__)
        """
        self.r_spec = Rectangle(1, 1)
        self.assertEqual(self.r_spec.display(), None)

    def test_Update(self):
        """python3 -c print(__import__("test_rectangle.py").Update.__doc__)
        """
        self.r6.update(10, 3)
        self.r7.update(21, 10, 8, 16)
        self.r8.update(1, 20, 10, 6, 9)
        a = self.r6
        b = self.r7
        c = self.r8
        b1 = b.width
        b2 = b.height
        b3 = b.x
        c1 = c.width
        c2 = c.height
        c3 = c.x
        c4 = c.y
        self.assertTrue(a.id == 10 and a.width == 3)
        self.assertTrue(b.id == 21 and b1 == 10 and b2 == 8 and b3 == 16)
        self.assertTrue(c.id == 1 and c1 == 20 and c2 == 10 and c3 == 6 and c4 == 9)

    @classmethod
    def tearDownClass(self):
        """python3 -c print(__import__("test_rectangle").tearDown.__doc__)
        """
        del self.r1, self.r2, self.r3
