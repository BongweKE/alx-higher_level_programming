#!/usr/bin/python3
"""Unit tests for instances of Square"""
import unittest
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

        def test_sub_class(self):
            """Confirnm that Rectangle is subclass of Base"""
            self.assertEqual(issubclass(Square, Rectangle), True)

if __name__ == "__main___":
    unittest.main()
