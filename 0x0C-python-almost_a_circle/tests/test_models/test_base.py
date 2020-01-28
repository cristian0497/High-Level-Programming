#!/usr/bin/python3
"""

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class Test_Base(unittest.TestCase):
    dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

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
