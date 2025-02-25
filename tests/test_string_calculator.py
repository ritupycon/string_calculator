import unittest

from src.string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = StringCalculator()
    
    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)
    
    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,5"), 6)
    
    def test_newline_separator(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)
    
    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("-1,-2")
        self.assertTrue("negative numbers not allowed -1, -2" in str(context.exception))
    
    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.add("//;\n1;2;3;4"), 10)
    
    def test_large_numbers(self):
        self.assertEqual(self.calc.add("1000,2000,3000"), 6000)
    
    def test_all_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("-1,-2,-3,-4")
        self.assertTrue("negative numbers not allowed -1, -2, -3, -4" in str(context.exception))

if __name__ == '__main__':
    unittest.main()