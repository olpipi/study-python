#!/bin/python

import unittest
import polynomial

class TestPolynomial(unittest.TestCase):

	def setUp(self):
		self.pm = polynomial.Polynomial([1, 2, 3, 4])
		pass

	def test_method__str__long(self):
		self.pm = polynomial.Polynomial(range(10))
		self.assertEqual(self.pm.__str__(), "x^8+2x^7+3x^6+4x^5+5x^4+6x^3+7x^2+8x+9")

	def tearDown(self):
		del self.pm
		pass


if __name__ == '__main__':
	unittest.main()