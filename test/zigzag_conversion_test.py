from unittest import TestCase
from ps.zigzag_conversion import convert
import unittest

class ZigzagConversionTest(TestCase):
    def test_1(self):
        self.assertEqual("PAHNAPLSIIGYIR", convert("PAYPALISHIRING", 3))
    def test_2(self):
        self.assertEqual("PINALSIGYAHRPI", convert("PAYPALISHIRING", 4))
        
if __name__ == '__main__':
    unittest.main()