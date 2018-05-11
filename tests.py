#!/bin/python

import unittest
from polynomial import Polynomial as Poly

class TestPolynomial(unittest.TestCase):

	def setUp(self):
		self.pm = Poly([1, 2, 3, 4])
		pass

	def tearDown(self):
		del self.pm
		pass

#test constructor and str
	def test_method_str_long(self):
		self.pm = Poly(range(10))
		self.assertEqual(self.pm.__str__(), "x^8+2x^7+3x^6+4x^5+5x^4+6x^3+7x^2+8x+9")

	def test_method_str_single_val(self):
		self.pm = Poly(76543)
		self.assertEqual(self.pm.__str__(), "76543")

	def test_method__str__list(self):
		self.assertEqual(self.pm.__str__(), "x^3+2x^2+3x+4")

	def test_method__str__list_float(self):
		self.pm = Poly([17.5, 1.3, -1.746, 8])
		self.assertEqual(self.pm.__str__(), "17.5x^3+1.3x^2-1.75x+8")

	def test_method_str_tuple(self):
		self.pm = Poly((1, 2, 3, 4))
		self.assertEqual(self.pm.__str__(), "x^3+2x^2+3x+4")


#test eq and ne
	def test_method_equal_long_true(self):
		self.pm = Poly(range(100))
		self.pm1 = Poly(range(100))
		self.assertTrue(self.pm1 == self.pm, "Error! Polynomials are equal")

	def test_method_equal_long_false(self):
		self.pm = Poly(range(100))
		self.pm1 = Poly(range(101))
		self.assertFalse(self.pm1 == self.pm, "Error! Polynomials are equal")

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

	def test_method_equal_single_val(self):
		self.pm = Poly([1])
		self.pm1 = Poly(1)
		self.assertTrue(self.pm == self.pm1, "Error! Polynomials aren't equal")


	def test_method_ne_long_false(self):
		self.pm = Poly(range(100))
		self.pm1 = Poly(range(101))
		self.assertTrue(self.pm != self.pm1, "Error! Polynomials aren't equal")

	def test_method_ne_long_true(self):
		self.pm = Poly(range(100))
		self.pm1 = Poly(range(100))
		self.assertFalse(self.pm != self.pm1, "Error! Polynomials aren't equal")

	def test_method_ne_list_tupl(self):
		self.pm1 = Poly((1, 2, 3, 5))
		self.assertTrue(self.pm1 != self.pm, "Error! Polynomials are equal")

	def test_method_ne_list_list(self):
		self.pm1 = Poly([1, 2, 3, 5])
		self.assertTrue(self.pm1 != self.pm, "Error! Polynomials are equal")

	def test_method_ne_list_str(self):
		self.pm1 = Poly("1, 2, 3, 5")
		self.assertTrue(self.pm1 != self.pm, "Error! Polynomials are equal")

# tests for + and +=
	def test_method_iadd_single_val(self):
		self.pm = Poly([1])
		self.pm1 = Poly("1")
		self.pm += self.pm1
		self.assertEqual(self.pm.__str__(), "2")

	def test_method_iadd_different_coeffs_num_1(self):
		self.pm = Poly([1, 2, 3, 4])
		self.pm1 = Poly([1, 2, 3, 4, 5])
		self.pm += self.pm1
		self.assertEqual(self.pm.__str__(), "x^4+3x^3+5x^2+7x+9")

	def test_method_iadd_different_coeffs_num_2(self):
		self.pm = Poly([1, 2, 3, 4, 5])
		self.pm1 = Poly([1, 2, 3, 4])
		self.pm += self.pm1
		self.assertEqual(self.pm.__str__(), "x^4+3x^3+5x^2+7x+9")

	def test_method__iadd__pm_and_float(self):
		self.pm = Poly([1, 2, 3, 4, 5, 6])
		self.pm += 1
		self.assertEqual(self.pm.__str__(), "x^5+2x^4+3x^3+4x^2+5x+7")

if __name__ == '__main__':
	unittest.main()