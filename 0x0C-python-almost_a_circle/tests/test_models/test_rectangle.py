#!/usr/bin/python3
"""
Unittest for Rectangle class
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
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

        # Test to_dictionary method
        self.assertEqual(
            Rectangle(4, 5, 6, 7, 7).to_dictionary(),
            {'x': 6, 'y': 7, 'id': 7, 'height': 5, 'width': 4})

        # test create method
        self.assertEqual(
            str(Rectangle.create(**{ 'id': 89 })),
            '[Rectangle] (89) 0/0 - 10/10')
        self.assertEqual(
            str(Rectangle.create(**{ 'id': 89, 'width': 1 })),
            '[Rectangle] (89) 0/0 - 1/10')
        self.assertEqual(
            str(Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })),
            '[Rectangle] (89) 0/0 - 1/2')
        self.assertEqual(
            str(Rectangle.create(
                **{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })),
            '[Rectangle] (89) 3/4 - 1/2')


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
        """Test for erroneous attrs"""
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
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(2, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def subclassIssues(self):
        """subclass tests"""
        self.assertEqual(issubclass(Rectangle, Base), True)

    def tests_that_open_file(self):
        """Test methods that save json to the file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, '[]')
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, '[]')
        Rectangle.save_to_file([Rectangle(1, 2)])
        s = '[{"x": 0, "y": 0, "id": 10, "height": 2, "width": 1}]'
        with open("Rectangle.json") as f:
            string_read = f.read()
            self.assertEqual(string_read, s)
        # test if load_from_file works on non existent files
        myfile = "Rectangle.json"
        if os.path.isfile(myfile):
            os.remove(myfile)
        self.assertEqual(Rectangle.load_from_file(), [])
        # load one rectangle and test whether it's well saved n loaded
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(
            [str(i) for i in Rectangle.load_from_file()],
            ['[Rectangle] (11) 0/0 - 1/2'])


    if __name__ == "__main___":
        unittest.main()
