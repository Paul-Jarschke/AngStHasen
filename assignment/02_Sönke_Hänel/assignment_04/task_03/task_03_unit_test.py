import unittest
from task_03_function import decimal2binary, decimal2binary_correct


class Dec2BinTestCase(unittest.TestCase):
    """Tests for 'task_03_function.py'."""

    def test_negative_input(self):
        """Do negative integers work?"""
        bin_out = decimal2binary(-1)
        self.assertEqual(bin_out, "-1")

    def test_zero_input(self):
        """Does zero work?"""
        bin_out = decimal2binary(0)
        self.assertEqual(bin_out, "0")

    def test_positive_input(self):
        """Do positive integers work?"""
        bin_out = decimal2binary(3)
        self.assertEqual(bin_out, "11")


class Dec2BinTestCase2(unittest.TestCase):
    """Tests for corrected 'task_03_function.py'."""

    def test_negative_input(self):
        """Do negative integers work?"""
        bin_out = decimal2binary_correct(-1)
        self.assertEqual(bin_out, "-1")

    def test_zero_input(self):
        """Does zero work?"""
        bin_out = decimal2binary_correct(0)
        self.assertEqual(bin_out, "0")

    def test_positive_input(self):
        """Do positive integers work?"""
        bin_out = decimal2binary_correct(3)
        self.assertEqual(bin_out, "11")
