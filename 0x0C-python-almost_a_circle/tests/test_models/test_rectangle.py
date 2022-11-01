#!/usr/bin/python3
"""Module for rectangle class instance"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_normal(self):
        r1  = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

if __name__ == '__main__':
    unittest.main()
