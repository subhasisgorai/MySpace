import unittest


def dutch_flag_partition(pivot_index, arr):
    pivot, smaller, equal, larger = (arr[pivot_index], 0, 0, len(arr))
    while equal < larger:
        if arr[equal] < pivot:
            arr[smaller], arr[equal] = arr[equal], arr[smaller]
            smaller += 1
            equal += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            arr[equal], arr[larger] = arr[larger], arr[equal]

            
class Test_Dutch_Partition(unittest.TestCase):

    def test_dutch_partition(self):
        arr = [-3, 0, -1, -1, -1, 2, 3, 4, 6, 5, -2, -1]
        dutch_flag_partition(2, arr)
        self.assertEqual(
            arr,
            [-3, -2, -1, -1, -1, -1, 4, 6, 5, 3, 2, 0])

            
if __name__ == '__main__':
    unittest.main()
