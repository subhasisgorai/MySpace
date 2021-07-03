from copy import copy
from collections import defaultdict

'''
    Given an array of n integers, how can we re-arrange the numbers in it such 
    that for any two numbers a [i] and a [j] (i < j), their average does not 
    lie between i and j. 
    This function has got an extremely poor time complexity of O(n.n!)
    Still thinking how we can make it efficient.
'''


def arrange_numbers_no_avg_in_between(arr):

    def permutations_helper(i):
        if i == len(arr) - 1:
            num_index_mapping = defaultdict(list)
            for idx, num in enumerate(arr):
                num_index_mapping[float(num)].append(idx)
                
            for start in range(len(arr) - 2):
                for end in range(start + 2, len(arr)):
                    avg = (float(arr[start]) + float(arr[end])) / 2
                    if any(start < idx < end for idx in num_index_mapping[avg]):
                        return
            return copy(arr)
        else:
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                result = permutations_helper(i + 1)
                if result:
                    return  result
                arr[i], arr[j] = arr[j], arr[i]
                
    return permutations_helper(0)


if __name__ == '__main__':
    print arrange_numbers_no_avg_in_between([1, 4, 2, 7])
    print arrange_numbers_no_avg_in_between([1, 201, 202, 431, 522])
    print arrange_numbers_no_avg_in_between(list(range(10)))
