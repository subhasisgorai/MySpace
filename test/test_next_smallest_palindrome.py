import unittest
from algo.next_smallest_palindrome import find_brute_force, find_optimized_manner


class TestNextSmallestPalindrome(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_optimized_method(self):
        samples = [111, 231598, 12345, 54792, 77777, 777777, 239756,
                        101010, 713322, 94187978149, 12345678, 89998, 899998, 888, 909, 122131, 1, 12]
        for sample in samples:
            print 'original {}, brute-force {}, optimized {}'.format(
                sample, find_brute_force(sample), find_optimized_manner(sample))
            self.assertEqual(find_brute_force(sample), find_optimized_manner(sample))
            
    def test_with_zero(self):
        self.assertEqual(find_brute_force(000), find_optimized_manner(000))
        
    def test_with_negative_integer(self):
        with self.assertRaises(AssertionError):
            find_optimized_manner(-12345)
        

if __name__ == '__main__': 
    unittest.main()
