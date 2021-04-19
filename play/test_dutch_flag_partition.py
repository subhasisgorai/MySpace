import unittest

from algo.dutch_flag import dutch_flag_partition


class Test(unittest.TestCase):

    def test_dutch_partition(self):
        arr = [-3, 0, -1, -1, -1, 2, 3, 4, 6, 5, -2, -1]
        dutch_flag_partition(2, arr)
        self.assertEqual(
            arr,
            [-3, -2, -1, -1, -1, -1, 4, 6, 5, 3, 2, 0])


if __name__ == "__main__":
    unittest.main()
