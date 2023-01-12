import unittest
from functions import decimal2binary, decimal_to_binary_correct


class Decimal2BinaryTestCase1(unittest.TestCase):
    """Test for decimal2binary function (fails)"""
    def test_negative_one_to_binary(self):
        """Test: -1 to -1"""
        result = decimal2binary(-1)
        self.assertEqual(-1, result)

    def test_zero_to_binary(self):
        """Test: 0 to 0"""
        result = decimal2binary(0)
        self.assertEqual(0, result)

    def test_one_to_binary(self):
        """Test: 1 to 1"""
        result = decimal2binary(1)
        self.assertEqual(1, result)

    def test_two_to_binary(self):
        """Test: 2 to 10"""
        result = decimal2binary(2)
        self.assertEqual(10, result)

    def test_three_to_binary(self):
        """Test: 3 to 11"""
        result = decimal2binary(3)
        self.assertEqual(11, result)


class Decimal2BinaryTestCase2(unittest.TestCase):
    """Test for decimal_to_binary_correct function (completes tests)"""
    def test_negative_one_to_binary(self):
        """Test: -1 to -1"""
        result = decimal_to_binary_correct(-1)
        self.assertEqual(-1, result)

    def test_zero_to_binary(self):
        """Test: 0 to 0"""
        result = decimal_to_binary_correct(0)
        self.assertEqual(0, result)

    def test_one_to_binary(self):
        """Test: 1 to 1"""
        result = decimal_to_binary_correct(1)
        self.assertEqual(1, result)

    def test_two_to_binary(self):
        """Test: 2 to 10"""
        result = decimal_to_binary_correct(2)
        self.assertEqual(10, result)

    def test_three_to_binary(self):
        """Test: 3 to 11"""
        result = decimal_to_binary_correct(3)
        self.assertEqual(11, result)
