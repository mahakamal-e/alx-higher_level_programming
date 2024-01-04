#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittest for max_integer([..])
    """

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        self.assertIsNone(max_integer([]))

    def test_None_input(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_integer(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 3, 4]), 4)

    def test_max_integer_(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([11, 9, 8]), 11)

    def test_string_(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(['Noha', 'ahmed', 'hassan']), 'hassan'
        )

    def test_raise_value_error(self):
        """test__max_integer__list_char_and_nums__raise_value_error"""
        with self.assertRaises(TypeError):
            max_integer(['Hala', 6, 'Walaa'])

    def test_raise_key_error(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(KeyError):
            max_integer({1: 'a', 2: 'b', 3: 'c'})

    def test_oneInteger(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([9]), 9)

    def test_float_int(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1.8, 17.5, -10, 9, 6]), 17.5)

    def test_error(self):
        """Unittest for max_integer([..])"""
        self.assertIsNone(max_integer(""))

    def test_max_char(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer('maha'), 'm')


if __name__ == '__main__':
    unittest.main()
