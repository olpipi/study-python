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


	def __str__(self):
		return self.polynomial_to_string()

	def __len__(self):
		return len(self.m_coeffs)

	def __eq__(self, pl):
		pl = Polynomial(pl)
		if len(pl) != len(self):
			return False
		for i, j in zip(self.m_coeffs, pl.m_coeffs):
			if i != j:
				return False
		return True

def __ne__(self, pl):
        pl = Polynomial(pl)
        return False if self.__eq__(pl) == True else True


if __name__ == "__main__":
	print("Main")