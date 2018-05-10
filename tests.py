#!/bin/python

import unittest
from polynomial import Polynomial as Poly

class TestPolynomial(unittest.TestCase):

	def setUp(self):
		self.pm = Poly([1, 2, 3, 4])
		pass

	def test_method__str__long(self):
		self.pm = Poly(range(10))
		self.assertEqual(self.pm.__str__(), "x^8+2x^7+3x^6+4x^5+5x^4+6x^3+7x^2+8x+9")

	def test_method_equal_list_tupl(self):
		self.pm1 = Poly((1, 2, 3, 4))
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_list_list(self):
		self.pm1 = Poly([1, 2, 3, 4])
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_list_range(self):
		self.pm1 = Poly(range(1,5))
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_list_str(self):
		self.pm1 = Poly("1, 2, 3, 4")
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def tearDown(self):
		del self.pm
		pass



if __name__ == '__main__':
	unittest.main()