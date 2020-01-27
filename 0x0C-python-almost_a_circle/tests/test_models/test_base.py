#!/usr/bin/python3
"""

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_Base(unittest.TestCase):
    dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}

    def test_Base(self):
        _1 = Base()
        self.assertEqual(_1.id, 1, msg="")
        _2 = Base()
        self.assertEqual(_2.id, 2, msg="")
        _3 = Base()
        self.assertEqual(_3.id, 3, msg="")
        _4 = Base(13)
        self.assertEqual(_4.id, 13, msg="")
        _5 = Base(None)
        self.assertNotEqual(_5.id, 1, msg="")

if __name__ == "__main__":
    unittest.main()
