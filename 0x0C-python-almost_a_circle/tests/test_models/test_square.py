#!/usr/bin/python3
"""python3 -c print(__import__("test_square.py").__doc__)
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """python3 -c print(__import__("test_square.py").TestSquare.__doc__)
    """
    @classmethod
    def setUpClass(self):
        """python3 -c print(__import__("test_square.py").setUpClass.__doc__)
        """
        self.s1 = Square(2, 3, 5, 6)
        self.s2 = Square(11, 29, 87, 66)
        self.s3 = Square(90, 91, 92, 93)

    @classmethod
    def tearDownClass(self):
        """python3 -c print(__import__("test_square.py").tearDownClass.__doc__)
        """
        del self.s1, self.s2, self.s3

    def test_SetGet(self):
        """python3 -c print(__import__("test_square.py").SetGet.__doc__)
        """
        a = self.s1
        b = self.s2
        c = self.s3

        self.assertEqual(a.id, 6)
        self.assertEqual(b.width, 11)
        self.assertEqual(c.x, 91)

    def test_Update(self):
        """python3 -c print(__import__("test_square.py").Update.__doc__)
        """
        self.s1.update(100)
        self.s2.update(1, 3, 4)
        self.s3.update(5, 32, 70, 4)

        self.assertEqual(self.s1.size, 100)
        self.assertTrue(self.s2.x == 3 and self.s2.y == 4)
        self.assertTrue(self.s3.id == 4 and self.s3.size == 5)
