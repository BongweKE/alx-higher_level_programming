#!/usr/bin/python3
"""Module for test of base.py"""
import unittest
from models.base import Base


class TestsForBaseClass(unittest.TestCase):
        """"Test Base class"""
        def test_normal(self):
            """Test expected usage scenarios"""
            r1 = Base()
            r2 = Base()
            r3 = Base(19)
            self.assertEqual(r1.id, 1)
            self.assertEqual(r2.id, 2)
            self.assertEqual(r3.id, 19)
            self.assertEqual(Base.to_json_string(None), '[]')
            self.assertEqual(Base.to_json_string([]), '[]')
            self.assertEqual(
                Base.to_json_string([ { 'id': 12 }]),
                                    '[{"id": 12}]')
            self.assertEqual(
                    type(Base.to_json_string([ { 'id': 12 }])), str)
            self.assertEqual(Base.from_json_string(None), [])
            self.assertEqual(Base.from_json_string("[]"), [])
            self.assertEqual(
                Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
            self.assertEqual(type(Base.from_json_string('[{ "id": 89 }]')),
                             list)

        def tests_for_negatives_and_float(self):
            """Test class float and negative attributes"""
            r1 = Base(-3)
            r2 = Base(9.9)
            self.assertEqual(r1.id, -3)
            self.assertEqual(r2.id, 9.9)

        def test_other_types(self):
            """Test non numerial types like lists and strings"""
            r1 = Base("one")
            r2 = Base({"number": 1})
            r3 = Base([1, 2])
            r4 = Base((1, 2))
            self.assertEqual(r1.id, "one")
            self.assertEqual(r2.id, {"number": 1})
            self.assertEqual(r3.id, [1, 2])
            self.assertEqual(r4.id, (1, 2))

        def test_id_equality(self):
            """Tests for Same id cases"""
            r1 = Base(2)
            r2 = Base(2)
            self.assertEqual(r1.id, 2)
            self.assertEqual(r2.id, 2)

if __name__ == "__main___":
    unittest.main()
