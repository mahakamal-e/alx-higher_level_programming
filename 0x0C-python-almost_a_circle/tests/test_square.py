#!/usr/bin/python3
""" unittest for Square class"""
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """ Test cases for class Square """
    def test_square_init(self):
        """test if class inherited from Base class"""
        s = Square(10)
        self.assertEqual(isinstance(s, Base), True)

    def test_square_no_arg(self):
        """ Test number of arguments """
        with self.assertRaises(TypeError):
            s = Square()

    def test_square_typeError(self):
        with self.assertRaises(TypeError):
            s = Square(9, 3, 1, 1, 1, "m")

    def test_size(self):
        s = Square(1)
        s.size = 9
        self.assertEqual(s.size, 9)

    def test_size_typeError(self):
        with self.assertRaises(TypeError):
            s = Square(9, 4.5, 1, 1, 2, 4)

    def test_size_typeError_bool(self):
        with self.assertRaises(TypeError):
            Square(True, 10, 0, 0, 9)

    def test_x(self):
        """test cases for x variable"""
        s = Square(5, 1)
        self.assertEqual(s.x, 1)

        s.x = 15
        self.assertEqual(s.x, 15)

    def test_x_valid(self):
        with self.assertRaises(TypeError):
            Square("invalid")

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_y(self):
        """test cases for y variable"""
        s = Square(1, 0, 20)
        self.assertEqual(s.y, 20)

        s.y = 15
        self.assertEqual(s.y, 15)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            Square("invalid")

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            Square(-5)

    def test_area(self):
        """test area method"""
        s = Square(10)
        self.assertEqual(s.area(), 100)

        s = Square(5)
        self.assertEqual(s.area(), 25)


class TestSquareDisplay(unittest.TestCase):
    """ Test cases for Method display """
    def test_display_with_arguments(self):
        with self.assertRaises(TypeError):
            s = Square(4)
            s.display('str')

    def test_display_with_zer0_x_zero_y(self):
        s = Square(4)
        expected_output = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_y(self):
        s = Square(4, 2, 0, 9)
        expected_output = "  ####\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_zero_x(self):
        s = Square(4, 0, 2, 9)
        expected_output = "\n\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_with_x_y(self):
        s = Square(4, 1, 2, 9)
        expected_output = "\n\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
