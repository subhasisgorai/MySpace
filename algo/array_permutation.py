from copy import copy
from pprint import pprint


def permute(arr):

    def permutation_helper(i):
        if i == len(arr) - 1:
            result.append(copy(arr))
            return
        for j in range(i, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            permutation_helper(i + 1)
            arr[i], arr[j] = arr[j], arr[i]
        
    result = list()
    permutation_helper(0)
    print 'for array: {}, permutations count: {}'.format(arr, len(result))
    return result


if __name__ == '__main__':
    pprint(permute([1, 2, 4, 7]), width=32)
    pprint(permute(list(range(5))), width=32)
