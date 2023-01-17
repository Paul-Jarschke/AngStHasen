import unittest
import binary

class TestDecimal(unittest.TestCase):

    def test_decimal_minusone(self):
        self.assertEqual(-1,binary.decimal2binary(-1))

    def test_decimal_zero(self):
        self.assertEqual(0,binary.decimal2binary(0))

    def test_decimal_one(self):
        self.assertEqual(1,binary.decimal2binary(1))

    def test_decimal_two(self):
        self.assertEqual(10,binary.decimal2binary(2))

    def test_decimal_three(self):
        self.assertEqual(11,binary.decimal2binary(3))

if __name__== '__main__':
    unittest.main()


class TestDecimal_corect(unittest.TestCase):

    def test_decimal_minusone(self):
        self.assertEqual(-1,binary.decimal2binary_correct(-1))

    def test_decimal_zero(self):
        self.assertEqual(0,binary.decimal2binary_correct(0))

    def test_decimal_one(self):
        self.assertEqual(1,binary.decimal2binary_correct(1))

    def test_decimal_two(self):
        self.assertEqual(10,binary.decimal2binary_correct(2))

    def test_decimal_three(self):
        self.assertEqual(11,binary.decimal2binary_correct(3))

if __name__== '__main__':
    unittest.main()
