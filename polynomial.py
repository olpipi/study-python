#!/bin/python

class Polynomial:
	
	def __init__(self, coeffs):
		self.m_coeffs = list()
		self.parse_coeffs(coeffs)

	def parse_coeffs(self, coeffs):
		if (type(coeffs) is list) or (type(coeffs) is tuple) or (type(coeffs) is range):
			for it in coeffs:
				self.m_coeffs.append(float(it))
		elif (isinstance(coeffs, Polynomial)):
			self.m_coeffs.extend(coeffs.m_coeffs)
		elif type(coeffs) is str:
			self.m_coeffs = [float(c) for c in coeffs.split(",")]
		elif (type(coeffs) is float) or (type(coeffs) is int):
			self.m_coeffs.append(float(coeffs))
		else:
			raise ValueError("Error! Unknown constructor")


	def polynomial_to_string(self, var_string = 'x', fraction = 2):
		if all(coeff == 0 for coeff in self.m_coeffs):
			return '0'
		
		res_str = ''
		first_pow = len(self) - 1
		
		for i, coeff in enumerate(self.m_coeffs):
			power = first_pow - i
			coeff = round(coeff, fraction)
			if coeff:
				if coeff < 0:
					sign = '-'
				elif coeff > 0:
					sign = ('+' if res_str else '')
				coeff = abs(coeff)
				if (coeff == 1) and (power != 0):
					str_coeff = ''
				elif (coeff == 0) and (power == 0):
					str_coeff = '0'
				else:
					int_str = str(str(coeff).split('.')[0])
					frac_str = str(str(coeff - (int(coeff) % int(int_str))).split('.')[1])
					str_coeff = int_str + ('' if frac_str == '0' else ('.' + frac_str))
				if power == 0:
					str_power = ''
				elif power == 1:
					str_power = var_string
				else:
					str_power = var_string + '^' + str(power)
				res_str += sign + str_coeff + str_power
		return res_str

	def add_zero_coeffs(self, other):
		if len(self) < len(other):
			self.m_coeffs.reverse()
			self.m_coeffs.extend([0 for i in range(len(other) - len(self))])
			self.m_coeffs.reverse()
		else:
			other.m_coeffs.reverse()
			other.m_coeffs.extend([0 for i in range(len(self) - len(other))])
			other.m_coeffs.reverse()

	def __str__(self):
		return self.polynomial_to_string()

	def __len__(self):
		return len(self.m_coeffs)

	def __eq__(self, other):
		other = Polynomial(other)
		if len(other) != len(self):
			return False
		for i, j in zip(self.m_coeffs, other.m_coeffs):
			if i != j:
				return False
		return True

	def __ne__(self, other):
		other = Polynomial(other)
		return False if self.__eq__(other) == True else True

	def __iadd__(self, other):
		other = Polynomial(other)
		finLen = max(len(self) , len(other))
		self.add_zero_coeffs(other)
		for cId in range(0, finLen):
			self.m_coeffs[cId] += other.m_coeffs[cId]
		return self

	def __add__(self, other):
		other = Polynomial(other)
		pm = Polynomial(self.m_coeffs)
		pm += other
		return pm

	def __radd__(self, other):
		other = Polynomial(other)
		pm = Polynomial(self.m_coeffs)
		other += pm
		return other

	def __isub__(self, other):
		other = Polynomial(other)
		finLen = max(len(self) , len(other))
		self.add_zero_coeffs(other)
		for it in range(0, finLen):
			self.m_coeffs[it] -= other.m_coeffs[it]
		return self

	def __sub__(self, other):
		other = Polynomial(other)
		pm = Polynomial(self.m_coeffs)
		pm -= other
		return pm

	def __rsub__(self, other):
		other = Polynomial(other.m_coeffs)
		pm = Polynomial(self.m_coeffs)
		other -= pm
		return other

	def __imul__(self, other):
		other = Polynomial(other)
		pm = Polynomial([0 for i in range(len(other) + len(self) - 1)])
		for i1, val1 in enumerate(self.m_coeffs):
			for i2, val2 in enumerate(other.m_coeffs):
				pm.m_coeffs[i1 + i2] += val1 * val2
		self.m_coeffs = []
		for it in pm.m_coeffs:
			self.m_coeffs.append(it)
		return self

	def __mul__(self, other):
		other = Polynomial(other)
		pm = Polynomial(self.m_coeffs)
		pm *= other
		return pm

	def __rmul__(self, other):
		other = Polynomial(other)
		pm = Polynomial(self.m_coeffs)
		other *= pm
		return other


if __name__ == "__main__":
	print("Main")