import unittest
from ps import longest_substring_with_unique_chars


class LongestSubstrWithUniqCharsTest(unittest.TestCase):

    def test_1(self):
        self.assertEqual(6, 
                         longest_substring_with_unique_chars.find_longest_chars_with_distinct_chars('subhasis'))
        
    def test_2(self):
        self.assertEqual(3, 
                         longest_substring_with_unique_chars.find_longest_chars_with_distinct_chars('abcabcbb'))

    def test_3(self):
        self.assertEqual(1, 
                         longest_substring_with_unique_chars.find_longest_chars_with_distinct_chars('bbbbb'))
    
    def test_4(self):
        self.assertEqual(3, 
                         longest_substring_with_unique_chars.find_longest_chars_with_distinct_chars('pwwkew'))
    
    def test_5(self):
        self.assertEqual(0, 
                         longest_substring_with_unique_chars.find_longest_chars_with_distinct_chars(''))
                
if __name__ == '__main__':
    unittest.main()
