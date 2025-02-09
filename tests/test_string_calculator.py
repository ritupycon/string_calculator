import unittest

from src.string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = StringCalculator()
    
    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

if __name__ == '__main__':
    unittest.main()