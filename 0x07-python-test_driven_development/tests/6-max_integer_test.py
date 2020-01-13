#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Tests for class
    """
    def test(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_2(self):
        self.assertEqual(max_integer([1, -3]), 1)

    def test_3(self):
        self.assertEqual(max_integer([1, -3]), 1)

    def test_4(self):
        self.assertEqual(max_integer([]), None)

    def test_5(self):
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_6(self):
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3"])
