import unittest
from algo.partition_equal_subset_sum import can_partition


class PartitionEqualSumTest(unittest.TestCase):
    
    def test_1(self):
        self.assertTrue(can_partition([1, 1, 3, 5]))
        self.assertTrue(can_partition([1, 7, 12, 4]))
        self.assertFalse(can_partition([1, 7, 12, 5]))
        self.assertTrue(can_partition([2, 2, 1, 1]))
        self.assertTrue(can_partition([23,13,11,7,6,5,5]))
