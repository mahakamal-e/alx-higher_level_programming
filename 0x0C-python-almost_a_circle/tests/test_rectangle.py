#!/usr/bin/python3
""" Test Module for class Rectangle """
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """ Unittest for Rectangle class """
    def test_rectangle_base(self):
        self.assertIsInstance(Rectangle(9, 2), Base)

    def test_init_rectangle(self):
        a1 = Rectangle(10, 12, 0, 0, 12)
        self.assertEqual(a1.id, 12)

    def tset_init_rectangle_arg(self):
        with self.assertRaises(TypeError):
            a = Rectangle(1)

    def test_init_rectangle_noArg(self):
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_width(self):
        a = Rectangle(2, 4)
        a.width = 10
        self.assertEqual(a.width, 10)

    def test_width_typeError(self):
        with self.assertRaises(TypeError):
            Rectangle([3.5, 3], 10, 0, 0, 11)

    def test_width_typeError_set(self):
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 10, 0, 0, 9)

    def test_width_typeError_dict(self):
        with self.assertRaises(TypeError):
            Rectangle({'a': 1, 'b': 2}, 10, 0, 0, 9)

    def test_width_INF(self):
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 10, 0, 0, 9)

    def test_width_with_negative(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 10, 0, 0, 9)

    def test_width_with_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 0, 0, 9)


if __name__ == '__main__':
    unittest.main()
