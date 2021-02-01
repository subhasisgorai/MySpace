'''
    The time complexity of this algorithm is not so intuitive. If you see for loop nesting with 
    while loop, you may think that the complexity of this algorithm is O(n^2), but in fact the 
    complexity of this algorithm is only O(n).
    To analyze its time complexity, we need to look at it on a whole: There are n elements in 
    total, each element is pushed into the stack once, and it will be pop once at most, without 
    any redundant operation. So the total calculation scale is proportional to the element scale n, 
    which is the complexity of O(n).
    
    Reference: https://labuladong.gitbook.io/algo-en/ii.-data-structure/monotonicstack
'''


def find_next_greater_element(arr):
    if arr:
        stack = list()
        result_arr = [None] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            result_arr[i] = -1 if not stack else stack[-1]
            stack.append(arr[i])
        return result_arr


def find_next_greater_element_in_circular_array(arr):
    if arr:
        n, stack = len(arr), list()
        result_arr = [None] * n
        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= arr[i % n]:
                stack.pop()
            result_arr[i % n] = -1 if not stack else stack[-1]
            stack.append(arr[i % n])
        return result_arr


if __name__ == '__main__':
    arr = [2, 1, 2, 4, 3]
    result = find_next_greater_element(arr)
    print result
    
    result = find_next_greater_element_in_circular_array(arr)
    print result
