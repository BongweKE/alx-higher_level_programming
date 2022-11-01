#!/usr/bin/python3
"""Unit tests for instances of Square"""
import unittest
import os
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestsForSquare(unittest.TestCase):
    """Test cases for square instances"""
    def test_normal(self):
        r1 = Square(5, 3, 1)
        self.assertEqual(r1.size, 5)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.area(), 25)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.size, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 89)
        r2 = Square(1)
        self.assertEqual(r2.size, 1)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        r3 = Square(1, 2)
        self.assertEqual(r3.size, 1)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 0)
        r5 = Square(1, 2, 3, 4)
        self.assertEqual(r5.size, 1)
        self.assertEqual(r5.x, 2)
        self.assertEqual(r5.y, 3)
        self.assertEqual(r5.id, 4)
        # test to_dictionary() method
        self.assertEqual(
            Square(4, 4, 7, 7).to_dictionary(),
            {'id': 7, 'x': 4, 'y': 7, 'size': 4})

        # test create method
        self.assertEqual(
            str(Square.create(**{ 'id': 89 })),
            '[Square] (89) 0/0 - 1')
        self.assertEqual(
            str(Square.create(**{ 'id': 89, 'size': 1 })),
            '[Square] (89) 0/0 - 1')
        self.assertEqual(
            str(Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })),
            '[Square] (89) 2/0 - 1')
        self.assertEqual(
            str(Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })),
            '[Square] (89) 2/3 - 1')

    def test_square_errors(self):
        """Test TypeErrors and ValueErrors"""
        with self.assertRaises(TypeError):
            Square("A")
        with self.assertRaises(TypeError):
            Square(1, "Gai")
        with self.assertRaises(TypeError):
            Square(1, 2, "Waah")
        with self.assertRaises(ValueError):
            Square(-13)
        with self.assertRaises(ValueError):
            Square(1, -27)
        with self.assertRaises(ValueError):
            Square(1, 2, -33)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test __str__ functionality """
        self.assertEqual(str(Square(1, 2, 3, 4)), "[Square] (4) 2/3 - 1")

    def test_sub_class(self):
        """Confirnm that Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Square, Rectangle), True)

    def tests_that_open_file(self):
        """Test methods that save json to the file"""
        Square.save_to_file([])
        with open("Square.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, '[]')
        Square.save_to_file([Square(1, 2)])
        s = '[{"id": 20, "x": 2, "y": 0, "size": 1}]'
        with open("Square.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, s)
        # test if load_from_file works on non existent files
        myfile = "Square.json"
        if os.path.isfile(myfile):
            os.remove(myfile)
        self.assertEqual(Square.load_from_file(), [])
        # load one rectangle and test whether it's well saved n loaded
        Square.save_to_file([Square(1, 2)])
        self.assertEqual(
            [str(i) for i in Square.load_from_file()],
            ['[Square] (21) 2/0 - 1'])

    def test_none(self):
        """Temp test to see issues"""
        Square.save_to_file(None)
        with open("Square.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, '[]')

if __name__ == "__main___":
    unittest.main()
