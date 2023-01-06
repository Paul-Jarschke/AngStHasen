import unittest
from decimal2binary_incorrect import decimal2binary


class TestConverter(unittest.TestCase):

    def test_minus_one(self):
        result = decimal2binary(-1)
        self.assertEqual(result, -1)

    def test_zero(self):
        result = decimal2binary(0)
        self.assertEqual(result, 0)

    def test_one(self):
        result = decimal2binary(1)
        self.assertEqual(result, 1)

    def test_two(self):
        result = decimal2binary(2)
        self.assertEqual(result, 10)

    def test_three(self):
        result = decimal2binary(3)
        self.assertEqual(result, 11)
