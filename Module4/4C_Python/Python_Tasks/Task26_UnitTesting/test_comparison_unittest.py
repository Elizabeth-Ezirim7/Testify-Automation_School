""""

Create a test case that compares two strings
Create another test case that compares different numbers

Use any unit testing framework from this week's lessons."""
import unittest

 # test_unittest_comparison.py
class ComparisonTest(unittest.TestCase):

    def compare_two_strings(self):
        string1 = "My Name Is Elizabeth"
        string2 = "I am a Qa Engineer"
        self.assertEqual(string1, string2)

    def compare_different_numbers(self):
        num1 = 10
        num2 = 20
        self.assertEqual(num1, num2)

if __name__ == '__main__':
    unittest.main()