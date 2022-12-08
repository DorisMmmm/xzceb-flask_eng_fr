'''Unit tests for translator.py'''
import unittest
import translator

from translator import french_to_english, english_to_french

class TranslatorTestClass(unittest.TestCase):

    def test_english_to_french(self):
        ''' test for English to French'''
        engl = english_to_french('Hello')
        frnc = french_to_english(engl)
        self.assertEqual(frnc, 'Bonjour')

    def test_english_to_french_not_equal(self):
        ''' test for English to French'''
        self.assertNotEqual(english_to_french("xxx"), "")

    def test_french_to_english(self):
        '''tests for French to English'''
        frnc = french_to_english('Bonjour')
        engl = english_to_french(frnc)
        self.assertEqual(engl, 'Hello')

    def test_french_to_english_not_equal(self):
        '''tests for French to English'''
        self.assertNotEqual(french_to_english("xxx"), "")

if __name__ == '__main__':
    unittest.main()
   
