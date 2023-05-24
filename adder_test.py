'''
Test the Adder function
'''
import adder
import unittest

class test_adder(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(add_nums(2,3),5)
        self.assertNotEqual(add_nums(1,7),5)
