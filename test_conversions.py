import unittest

from roman_numerals import RomanError, arabic_to_roman, roman_to_arabic

class Test_arabic_to_roman_functions(unittest.TestCase):
    def test_arabic_to_roman_without_subtraction(self):
        self.assertEqual(arabic_to_roman(36),'XXXVI')

    def test_arabic_to_roman_with_subtraction(self):
        self.assertEqual(arabic_to_roman(464), 'CDLXIV')
    
    def test_arabic_to_roman_only_integers(self):
        with self.assertRaises(TypeError):
                arabic_to_roman('string')

    def test_arabic_to_roman_only_positive_integers(self):
        with self.assertRaises(ValueError):
                arabic_to_roman(-23)

class Test_roman_to_arabic_functions(unittest.TestCase):
    def test_roman_to_arabic_tree_repetitions_ok(self):
        self.assertEqual(roman_to_arabic('III'), 3)

    def test_roman_to_arabic_tree_repetitions_error(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('IIII')

    def test_roman_to_arabic_two_reppetitions_of_VLD_error(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('VV')
        with self.assertRaises(RomanError):
            roman_to_arabic('LL')
        with self.assertRaises(RomanError):
            roman_to_arabic('DD')
    
    def test_roman_to_arabic_VLD_no_subtraction(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('VX')
        with self.assertRaises(RomanError):
            roman_to_arabic('LC')
        with self.assertRaises(RomanError):
            roman_to_arabic('DM')

    def test_roman_to_arabic_after_reppetittion_does_not_remain(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('XXL')

        self.assertEqual(roman_to_arabic('XXIII'), 23)

    def test_roman_to_arabic_prohibited_subtractions_if_the_diference_is_high(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('XM')

    def test_roman_to_arabic_incorrect_symbols(self):
        with self.assertRaises(RomanError):
            roman_to_arabic('IK')
        with self.assertRaises(RomanError):
            roman_to_arabic('KI')
        with self.assertRaises(RomanError):
            roman_to_arabic('K')

    def test_roman_to_arabic_above_3999(self):
        self.assertEqual(roman_to_arabic("(IV)CCCXXIX"), 4329 )