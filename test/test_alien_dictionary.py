import unittest

from play.alien_dictionary_leetcode import alienOrder


class Test(unittest.TestCase):

    def testAlienOrdering(self):
        self.assertEquals(alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']), 'wertf')
        self.assertEquals(alienOrder(['z', 'x']), 'zx')
        self.assertEquals(alienOrder(['z', 'x', 'z']), '')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
