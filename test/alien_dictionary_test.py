from __future__ import absolute_import
import unittest

from play.alien_dictionary_leetcode import alienOrder


class Test(unittest.TestCase):

    def testAlienOrdering(self):
        self.assertEqual(alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')
        self.assertEqual(alienOrder(['z', 'x']), 'zx')
        self.assertEqual(alienOrder(['z', 'x', 'z']), '')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
