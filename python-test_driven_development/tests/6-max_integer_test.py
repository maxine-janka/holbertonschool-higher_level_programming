#!/usr/bin/python3
"""unittests for the function max_integer(list=[])"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer_ordered(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer_unordered(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
    
    def test_max_integer_negative(self):
        """Test a list of negative integers"""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
    
    def test_max_integer_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.1, 3.2, 4.6, 2.5]), 4.6)
    
    def test_max_integer_one_element(self):
        """Test one element in list"""
        self.assertEqual(max_integer([1]), 1)
    
    def test_max_integer_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_max_integer_wrong_type(self):
        """Test list containing non-integers"""
        with self.assertRaises(TypeError):
            max_integer(([1, "3", 4, 2]), 4)

if __name__ == '__main__':
    unittest.main()
