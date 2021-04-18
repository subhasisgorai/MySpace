def canJump(nums):

    def dfs_helper(node):
        if node == dest:
            return True
        if node > len(nums) - 1 or nums[node] == 0:
            return False
        
        visited.add(node)
        return any([dfs_helper(node + i) for i in range(1, nums[node] + 1) if node + i not in visited])
    
    src, dest, visited = 0, len(nums) - 1, set()
    return dfs_helper(src)


def canJump_no_recurion(nums):
    if len(nums) == 1:
        return True
    
    stack, visited = list([0]), set()
    while stack:
        popped = stack.pop()
        if popped == len(nums) - 1:
            return True
        for i in range(1, nums[popped] + 1):
            if popped + i >= len(nums) - 1:
                return True
            if popped + i not in visited:
                stack.append(popped + i)
        visited.add(popped)
    
    return False


def canJump_DP(self, nums):
        result = [None] * (len(nums) - 1) + [True]
        for i in range(len(nums) - 2, -1, -1):
            farthest_reach = min(len(nums) - 1, i + nums[i])
            for position in range(i + 1, farthest_reach + 1):
                if result[position]:
                    result[i] = True
                    break
        return result[0]


if __name__ == '__main__':
    print canJump_no_recurion([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    print canJump_no_recurion([1, 1, 1, 1, 1, 1])
    print canJump_no_recurion([3, 2, 1, 0, 4])
