#!/bin/python

import unittest
import polynomial as poly

class TestPolynomial(unittest.TestCase):

	def setUp(self):
		self.pm = poly.Polynomial([1, 2, 3, 4])
		pass

	def test_method__str__long(self):
		self.pm = poly.Polynomial(range(10))
		self.assertEqual(self.pm.__str__(), "x^8+2x^7+3x^6+4x^5+5x^4+6x^3+7x^2+8x+9")

	def test_method_equal_tupl(self):
		self.pm1 = poly.Polynomial((1, 2, 3, 4))
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_list(self):
		self.pm1 = poly.Polynomial([1, 2, 3, 4])
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_range(self):
		self.pm1 = poly.Polynomial(range(4))
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")


	def tearDown(self):
		del self.pm
		pass



if __name__ == '__main__':
	unittest.main()