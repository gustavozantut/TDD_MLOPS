import unittest
from roman_numbers04 import RomanNumbers

class FibonacciTest(unittest.TestCase):

    def test_input_number(self):
        self.assertEqual(RomanNumbers.get_number_from_roman(4), "entrada inválida")

    def test_invalid_letters(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("gustavo"), "entrada inválida")

    def test_valid_input(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("VI"), 6)
        