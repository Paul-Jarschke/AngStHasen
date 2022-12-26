import unittest
from . import function as f


class Decimal2BinaryTestCase(unittest.TestCase):
    """Test for function.py (includes decimal2binary function)"""
    def test_negative_one_to_binary(self):
        """Test if -1 is converted to -1"""
        result = f.decimal2binary(-1)
        self.assertEqual(-1, result)

    def test_zero_to_binary(self):
        """Test if 0 is converted 0"""
        result = f.decimal2binary(0)
        self.assertEqual(0, result)

    def test_one_to_binary(self):
        """Test if 1 is converted to 1"""
        result = f.decimal2binary(1)
        self.assertEqual(1, result)

    def test_two_to_binary(self):
        """Test if 2 is converted to 10"""
        result = f.decimal2binary(2)
        self.assertEqual(10, result)

    def test_three_to_binary(self):
        """Test if 3 is converted to 11"""
        result = f.decimal2binary(3)
        self.assertEqual(11, result)