from collections import defaultdict


def subarray_sum(arr, k):
    prefix_sum = defaultdict(int)
    prefix_sum[0] = 1
    sum_i = ans = 0
    for i in arr:
        sum_i += i
        sum_j = sum_i - k
        ans += prefix_sum[sum_j]
        prefix_sum[sum_i] += 1
    
    return ans


if __name__ == '__main__':
    print subarray_sum([1, 1, 1], 2)
    print subarray_sum([1, 2, 3, 4, 5], 15)
