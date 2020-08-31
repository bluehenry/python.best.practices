import unittest
import numpy as np
from sklearn import linear_model

from polynomial_regression import *

class PolynomialRegressionTest (unittest.TestCase):

    def test_case1(self):
        self.assertEqual(polynomial_regression(), 1)

if __name__ == '__main__':
        unittest.main()