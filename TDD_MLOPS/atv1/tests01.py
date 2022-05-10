import unittest
from roman_numbers01 import RomanNumbers

class FibonacciTest(unittest.TestCase):

    def test_input(self):
    	self.assertEqual(RomanNumbers.get_number_from_roman(4), "caractér inválido")