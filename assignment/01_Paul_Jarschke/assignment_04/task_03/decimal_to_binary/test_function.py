import unittest
import sys
import os
# set parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from function import decimal2binary


class Decimal2BinaryTestCase(unittest.TestCase):
    """Test for function.py (includes decimal2binary function)"""
    def test_negative_one_to_binary(self):
        result = decimal2binary(-1)
        self.assertTrue(-1)
