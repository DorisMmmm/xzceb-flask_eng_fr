""" Unit tests """
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ English to French """
    def test_is_not_none(self):
        self.assertIsNotNone(english_to_french('Hello'))
    def test_is_equal(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_is_not_equal(self):
        self.assertNotEqual(english_to_french('Lederhosen'),'Hallo')

class TestFrenchToEnglish(unittest.TestCase):
    """ French to English """
    def test_is_not_none(self):
        self.assertIsNotNone(french_to_english('Bonjour'))
    def test_is_equal(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_is_not_equal(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Gruezi')

unittest.main()
