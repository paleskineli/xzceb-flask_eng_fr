import unittest
from translator import english_to_french, french_to_english

class TestEnglish(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french('None'), '')
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestFrench(unittest.TestCase):
    def test_french_to_english(self):
        self.assertNotEqual(french_to_english('None'), '')
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
    
    
