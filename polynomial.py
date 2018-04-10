#!/bin/python

class Polynomial:
	
	def __init__(self, coeffs):
		self.m_coeffs = list()
		for it in coeffs:
			self.m_coeffs.append(float(it))

		
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


if __name__ == "__main__":
	print("Main")