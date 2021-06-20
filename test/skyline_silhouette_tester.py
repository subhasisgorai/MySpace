import unittest

from algo.skyline_silhouette import get_skyline_silhouette


class SkylineSilhouetteTester(unittest.TestCase):

    def test_1(self):        buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        expected_output = [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
        actual_output = get_skyline_silhouette(buildings)
        self.assertEquals(actual_output, expected_output)

    def test_2(self):
        buildings = [[0, 2, 3], [2, 5, 3]]
        expected_output = [[0, 3], [5, 0]]
        actual_output = get_skyline_silhouette(buildings)
        self.assertEquals(actual_output, expected_output)
        
    def test_3(self):
        buildings = []
        self.assertIsNone(get_skyline_silhouette(buildings))
        
    def test_4(self):
        buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
        expected_output = [[1, 3], [2, 0]]
        actual_output = get_skyline_silhouette(buildings)
        self.assertEquals(actual_output, expected_output)

    def test_5(self):
        buildings = [[1, 5, 3], [1, 5, 3], [1, 5, 3]]
        expected_output = [[1, 3], [5, 0]]
        actual_output = get_skyline_silhouette(buildings)
        self.assertEquals(actual_output, expected_output)
        
if __name__ == "__main__":
    unittest.main()