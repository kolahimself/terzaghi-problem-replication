"""
Module containing the methods used in my problem simulation
"""
import numpy as np
from table_vals import phi_to_Nq
class Methods:
	@staticmethod
	def sin(phi: float) -> float:
		return np.sin(np.radians(phi))

	def default_check(text: str) -> float:
		if text == "":
			text = 0
		else:
			text = float(text)
		return text

	@staticmethod
	def compute_nq(phi: float) -> float:
		exponent = 2 * ((0.75 * np.pi) - (phi/2)) * np.tan(np.radians(phi))
		numerator = np.exp(exponent)
		denominator = 2 * np.square((np.cos(np.radians(45 + (phi/2)))))
		Nq = numerator / denominator
		return [Nq, numerator, denominator]

	def check_nq_from_table(phi: int) -> float:
		return phi_to_Nq[phi]


methods = {
	"sin": Methods.sin,
	"check": Methods.default_check,
	"Nq": Methods.compute_nq,
	"nq_from_table": Methods.check_nq_from_table
}
