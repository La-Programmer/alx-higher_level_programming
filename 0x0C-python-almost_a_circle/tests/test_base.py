#!/usr/bin/python3
"""python3 -c 'print(__import__("test_base.py").__doc__)'
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """python3 -c 'print(__import__("test_base.py").TestBase.__doc__)'
    """

    def setUp(self):
        """python3 -c 'print(__import__("test_base.py").setUp.__doc__)'
        """
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(144)
        self.b4 = Base()

    def test_id(self):
        """python3 -c 'print(__import__("test_base.py").test_id.__doc__)'
        """
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 144)
        self.assertEqual(self.b4.id, 3)

    def tearDown(self):
        """python3 -c 'print(__import__("test_base.py").tearDown.__doc__)'
        """
        del self.b1, self.b2, self.b3, self.b4
