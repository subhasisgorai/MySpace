

def can_partition(nums):

    def summation_helper_count_ways(target):
        count_ways = [[0] * (target + 1) for _ in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] > j:
                    count_ways[i][j] = count_ways[i - 1][j] if i >= 1 else 0
                else:
                    count_ways[i][j] = ((count_ways[i - 1][j] if i >= 1 else 0) + 
                                                (1 if nums[i - 1] == j else 0) + 
                                                (count_ways[i - 1][j - nums[i - 1]] if i >= 1 else 0))
                
        return count_ways[len(nums)][target]
    
    if nums:
        total = sum(nums)
        if total % 2:
            return False
        sub_sum = total // 2
        return summation_helper_count_ways(sub_sum) >= 1
    return False


if __name__ == '__main__':
    # print 'Can partition {} into two equal subset:  {}'.format([1, 5, 11, 5],
    #                                                            can_partition([1, 5, 11, 5]))
    
    nums = [1, 1, 3, 5]
    print 'Can partition {} into two equal subset:  {}'.format(nums,
                                                               can_partition(nums))
    nums = [1, 7, 12, 4]
    print 'Can partition {} into two equal subset:  {}'.format(nums,
                                                               can_partition(nums))
    nums = [1, 7, 12, 5]
    print 'Can partition {} into two equal subset:  {}'.format(nums,
                                                               can_partition(nums))
