import unittest
from roman_numbers12 import RomanNumbers

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

    def test_valid_input_5(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("XXX"), 30)

    def test_valid_input_6(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("XXX"), 30)

    def test_valid_input_7(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("MMMCMXCIX"), 3999)    

    def test_invalid_input_2(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("MMMMMXCIX"), "entrada inválida")

    def test_valid_input_8(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("CCCIL"), 349)     
    
    def test_invalid_input_3(self):
        self.assertEqual(RomanNumbers.get_number_from_roman(12), "entrada inválida")   

    def test_valid_input_9(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("M*M*M*C*M*X*C*I*X*"), 3999000) 

    def test_valid_input_10(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("M*IX*"), 1009999)   

    def test_invalid_input_4(self):
        self.assertEqual(RomanNumbers.get_number_from_roman("MX**"), "entrada inválida")   
    
    def test_invalid_input_5(self):
        self.assertEqual(RomanNumbers.get_numbe_from_roman("*M*IX*"), "entrada inválida")       