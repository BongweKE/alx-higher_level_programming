#!/usr/bin/python3
"""Unittest for max_integer([..])

This module is used to conduct tests on edgecases for the imported
function ''max_integer()''

Example:
    It is expected that this module is with other tests
    $ python3 -m unittest tests.6-max_integer_test

Attributes:

    max_integer (function): the function fixture used in unittest
    bad_patterns (list): list of wrong input to max_integer()
    key_error_list (dict): dict to prove max_integer() can't use em
    str_patterns (list): list of patterns that behave like str
    num_patterns (list): list of lists of numbers to prove correct
    functionality of the function
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

bad_patterns = [1, 0.1, [1, []], [1, "str"], (2, "str")]

key_error_list = {'s': 3, 't': 3}

str_patterns = ["str", list("str"), ('s', 't', 'r'), "12.4t"]

num_patterns = [[4], [0.4, 0.6, 4.0], (0.1, 4.0)]


class TestMaxInteger(unittest.TestCase):
    """A class to hold all testcases for unitttest"""

    def test_Bad_Inputs(self):
        """Test patterns expected to raise errors
        First we show TypeError then KeyError"""
        for bad_pat in bad_patterns:
            with self.subTest(pattern=bad_pat):
                self.assertRaises(
                    TypeError,
                    max_integer,
                    bad_pat,
                )

        self.assertRaises(
            KeyError,
            max_integer,
            key_error_list,
        )

    def test_strings(self):
        """Test how strings wierdly still work with max_integer()"""
        for str_pat in str_patterns:
            with self.subTest(pattern=str_pat):
                self.assertEqual(
                    max_integer(str_pat),
                    "t")

    def test_numbers(self):
        """Test expected correct functionality of max_integer()
        First with no input then with various lists or tuples of numbers
        """
        self.assertEqual(
            max_integer(),
            None
        )
        for num_pat in num_patterns:
            with self.subTest(pattern=num_pat):
                self.assertEqual(
                    max_integer(num_pat),
                    4,
                )
