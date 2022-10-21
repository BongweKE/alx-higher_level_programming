#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

bad_patterns = [1, 0.1, [1, []], [1, "str"], (2, "str")]

key_error_list = {'s':3, 't':3}

str_patterns = ["str", list("str"), ('s', 't', 'r'), "12.4t"]

num_patterns = [[4], [0.4, 0.6, 4.0], (0.1, 4.0)]
class TestMaxInteger(unittest.TestCase):

    def test_Bad_Inputs(self):
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
        for str_pat in str_patterns:
            with self.subTest(pattern=str_pat):
                self.assertEqual(
                    max_integer(str_pat)
                    , "t")

    def test_numbers(self):
        self.assertEqual(
            max_integer(),
            None
        )
        for num_pat in num_patterns:
            with self.subTest(pattern = num_pat):
                self.assertEqual(
                    max_integer(num_pat),
                    4,
                )
