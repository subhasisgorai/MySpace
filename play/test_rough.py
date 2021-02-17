import unittest
import rough_book


class Tester(unittest.TestCase):

    def test_n_queens(self):
        self.assertTrue(multi_contains(rough_book.n_queens(4),
                                       [1, 3, 0, 2], [2, 0, 3, 1]))


def multi_contains(collection, *args):
    return all(item in collection for item in args)


if __name__ == '__main__':
    unittest.main()
