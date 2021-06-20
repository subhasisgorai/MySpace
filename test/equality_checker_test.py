import unittest
from play.equality_checker import check_equality


class TestEqualityChecker(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_transitive_equality(self):
        self.assertTrue(check_equality(['a=b', 'b=c', 'c=d', 'd=e', 'b=z'], 'a', 'z'))

    def test_inequality(self):
        self.assertFalse(check_equality(['a=b', 'b=c', 'c=d', 'd=e', 'b=z', 'x=y'], 'a', 'x'))
        
    def test_returns_none_for_empty_samples(self):
        self.assert_(check_equality(None, 'a', 'x') is None)
    
    def test_return_none_for_none_params(self):
        self.assert_(check_equality(['a=b'], None, 'x') is None)
        self.assert_(check_equality(['a=b'], 'a', None) is None)


if __name__ == '__main__':
    unittest.main()
    
