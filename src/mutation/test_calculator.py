from unittest import TestCase
from calculator import *

class CalculatorTest(TestCase):

    def test_mul(self):
        self.assertEqual(mul(2, 3), 6)

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(3, 2), 1.5)

    def test_difference(self):
        self.assertEqual(difference(2, 3), -1)

    def test_multiply_matrix_3x3(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = [[30, 36, 42], [66, 81, 96], [102, 126, 150]]
        multiplication_result = multiply_matrix_3x3(a, a)
        self.assertEqual(multiplication_result[0], result[0])
        self.assertEqual(multiplication_result[1], result[1])
        self.assertEqual(multiplication_result[2], result[2])

