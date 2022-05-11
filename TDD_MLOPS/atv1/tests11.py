import unittest
from roman_numbers11 import RomanNumbers

class RomanNumbersTest(unittest.TestCase):

    def test_input_number(self):
        self.assertEqual(RomanNumbers.get_number_from_roman(4), "entrada inválida")

    def test_invalid_letters(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("gustavo"), "entrada inválida")

    def test_half_invalid_letters(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("IVG"), "entrada inválida")

    def test_valid_input_1(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("VI"), 6)

    def test_invalid_input_valid_caract(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("IIII"), "entrada inválida")

    def test_valid_input_2(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("V"), 5)
    
    def test_valid_input_3(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("IV"), 4)

    def test_valid_input_4(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("XIV"), 14)