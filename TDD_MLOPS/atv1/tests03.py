import unittest
from roman_numbers03 import RomanNumbers

class FibonacciTest(unittest.TestCase):

    def test_input_number(self):
    	self.assertEqual(RomanNumbers.get_number_from_roman(4), "entrada inválida")

    def test_invalid_letters(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("gustavo"), "entrada inválida")