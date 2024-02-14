#!/usr/bin/python3
""" Unittest for Base class """
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ Define class to test cases"""
    def test_init(self):
        new_instance = Base()
        self.assertEqual(new_instance.id, 1)

        new_instance2 = Base()
        self.assertEqual(new_instance2.id, 2)

        new_instance3 = Base()
        self.assertEqual(new_instance3.id, 3)

    def test_to_json_string(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_NoneList(self):
        # Test case for to_json_string with None input
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_emptylist(self):
        # Test case for to_json_string with an empty list input
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string_NoneList(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_emptylist(self):
        self.assertEqual(Base.from_json_string([]), [])


if __name__ == "__main__":
    unittest.main()
