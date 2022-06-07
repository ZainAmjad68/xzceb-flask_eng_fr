import unittest

try:
    from translator import english_to_french, french_to_english
except ImportError:
    from .translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def testAssert(self):
        self.assertEqual(english_to_french("Hello"), '"Bonjour"')
        self.assertEqual(english_to_french(
            'Hello, how are you?'), '"Bonjour, comment es-tu?"')

    def testNull(self):
        self.assertEqual(english_to_french(None), 'Invalid Argument')


class TestFrenchToEnglish(unittest.TestCase):
    def testAssert(self):
        self.assertEqual(french_to_english("Bonjour"), '"Hello"')
        self.assertEqual(french_to_english(
            'Bonjour, comment es-tu?'), '"Hello, how are you?"')

    def testNull(self):
        self.assertEqual(french_to_english(None), 'Invalid Argument')


unittest.main()
