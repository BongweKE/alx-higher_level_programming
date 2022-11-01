#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base

class TestsForRectangle(unittest.TestCase):
    """Tests for rectangle"""
    def test_normal_ones(self):
        """Tests for normal cases"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(str(Rectangle(10, 2, 0, 0, 12)),
                    '[Rectangle] (12) 0/0 - 10/2')

        r1.update(13, 20, 4, 1, 1)
        self.assertEqual(r1.width, 20)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 13)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_no_x_y(self, mock_stdout):
        """Function to test how display method works"""
        Rectangle(3, 1).display()
        self.assertEqual(mock_stdout.getvalue(), "###\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_no_y(self, mock_stdout):
        """Function to test how display method works"""
        Rectangle(3, 1, 1).display()
        self.assertEqual(mock_stdout.getvalue(), " ###\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        """Function to test how display method works"""
        Rectangle(3, 1, 1, 1).display()
        self.assertEqual(mock_stdout.getvalue(), "\n ###\n")

    def test_error_msgs(self):
        """Test for erroneous errors"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(0.5, 10, 5, 5)
        with self.assertRaises(TypeError):
            r2 = Rectangle(4, 8.8, 5, 5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, 10, 5.9, 5)
        with self.assertRaises(TypeError):
            r2 = Rectangle(4, 8, 5, 7.5)
        with self.assertRaises(ValueError):
            Rectangle(-5, 1, 8, 9)
        with self.assertRaises(ValueError):
            Rectangle(5, -1, 80, 9)
        with self.assertRaises(ValueError):
            Rectangle(5, 1, -86, 9)
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 84, -9)

    def subclassIssues(self):
        """subclass tests"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    if __name__ == "__main___":
        unittest.main()
