import unittest
from roman_numbers08 import RomanNumbers

class RomanNumbersTest(unittest.TestCase):

    def test_input_number(self):
        print('teste1')
        self.assertEqual(RomanNumbers.get_number_from_roman(4), "entrada inválida")

    def test_invalid_letters(self):
        print('teste2')
        self.assertEqual(RomanNumbers.get_number_from_roman("gustavo"), "entrada inválida")

    def test_half_invalid_letters(self):
        print('teste3')
        self.assertEqual(RomanNumbers.get_number_from_roman("IVG"), "entrada inválida")

    def test_valid_input_1(self):
        print('teste4')
        self.assertEqual(RomanNumbers.get_number_from_roman("VI"), 6)

    def test_invalid_input_valid_caract(self):
        print('teste5')
        self.assertEqual(RomanNumbers.get_number_from_roman("IIII"), "entrada inválida")

    def test_valid_input_2(self):
        print('teste6')
        self.assertEqual(RomanNumbers.get_number_from_roman("V"), 5)