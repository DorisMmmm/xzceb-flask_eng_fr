'''Unit tests for translator.py'''
import unittest
import translator

from translator import french_to_english, english_to_french

class TranslatorTestClass(unittest.TestCase):

    def test_english_to_french(self):
        ''' test for English to French'''
        self.assertEqual(english_to_french(""), "")
        engl = english_to_french('Hello')
        frnc = french_to_english(engl)
        self.assertEqual(frnc, 'Bonjour')

    def test_french_to_english(self):
        '''tests for French to English'''

        self.assertEqual(french_to_english(""), "")
        frnc = french_to_english('Bonjour')
        engl = english_to_french(frnc)
        self.assertEqual(engl, 'Hello')


if __name__ == '__main__':
    unittest.main()
    