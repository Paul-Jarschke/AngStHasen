import unittest
from decimal2binary_correct import decimal_to_binary_correct


class TestConverter(unittest.TestCase):

    def test_minus_one(self):
        result = decimal_to_binary_correct(-1)
        self.assertEqual(result, -1)

    def test_zero(self):
        result = decimal_to_binary_correct(0)
        self.assertEqual(result, 0)

    def test_one(self):
        result = decimal_to_binary_correct(1)
        self.assertEqual(result, 1)

    def test_two(self):
        result = decimal_to_binary_correct(2)
        self.assertEqual(result, 10)

    def test_three(self):
        result = decimal_to_binary_correct(3)
        self.assertEqual(result, 11)
