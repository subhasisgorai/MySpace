from collections import deque
from collections import namedtuple
from copy import copy
# from pprint import pprint


def n_queens(n): 

    def get_queens_placement(row):
        if row == n:
            result.append(copy(col_placement))
            return 
        for col in range(n):
            if all(abs(col - c) not in (0, row - i)
                    for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                get_queens_placement(row + 1)
    
    result = list()
    col_placement = [0] * n
    get_queens_placement(0)
    return result


Item = namedtuple('Item', ('weight', 'value'))


def knapsack_with_repetition(items, max_weight):
    if items:
        max_value = list()
        max_value.append(0)
        for w in range(1, max_weight + 1):
            max_values = [max_value[w - item.weight] + item.value for item in filter(lambda item: item.weight <= w, items)]
            max_value.append(max(max_values) if max_values else 0)
        print max_value
        return max_value[max_weight]
    return 0


def knapsack_without_repetition(items, max_weight):
    if items:
        max_value = [[0] * (len(items) + 1) for _ in range(max_weight + 1)]
        for j in range(1, len(items) + 1):
            for w in range(1, max_weight + 1):
                if items[j - 1].weight > w:  # j-1 as the array index starts at 0
                    max_value[w][j] = max_value[w][j - 1]
                else:
                    max_value[w][j] = max(max_value[w][j - 1],
                                          max_value[w - items[j - 1].weight][j - 1] + items[j - 1].value)
        return max_value[max_weight][len(items)]
    return 0

# from pprint import pprint
Node = namedtuple('Node', ('x', 'y'))


def numIslands(grid):

        def neighbors(current_node):
            return [node for node in 
                        map(Node,
                            (current_node.x - 1, current_node.x + 1, current_node.x, current_node.x),
                            (current_node.y, current_node.y, current_node.y - 1, current_node.y + 1))
                        if node in all_nodes
                   ]
        
        if grid:
            all_nodes = [Node(x, y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == "1"]
            q, nodes_visited_already, island_count = deque(), [], 0
            
            for node in all_nodes:
                if node not in nodes_visited_already:
                    island_count += 1
                    q.append(node)
                    
                    while q:
                        n = q.popleft()
                        for neighbor in neighbors(n):
                            if neighbor not in nodes_visited_already:
                                q.append(neighbor)   
                        nodes_visited_already.append(n)
                    
                    q.clear()
                        
            return island_count
                         
        return 0

    
def levensthein_distance(word1, word2):
    if word1 == word2:
        return 0

    len1, len2 = len(word1), len(word2) 
    result = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    for i in range(len1 + 1):
        result[i][0] = i
    
    for j in range(len2 + 1):
        result[0][j] = j
        
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            result[i][j] = min(
                1 + result[i - 1][j],
                1 + result[i][j - 1],
                result[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
            )
    return result[len1][len2]


def find_next_greater_element(arr, element):
    if arr:
        mono_stack = list()
        result = [None] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            while mono_stack and mono_stack[-1] <= arr[i]:
                mono_stack.pop()
            result[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(arr[i])
        
        for i, item in enumerate(arr):
            if item is element:
                return result[i]    
        
    return -1


def find_next_greater_element_in_circular_array(arr, element):
    if arr:
        result = [None] * len(arr)
        mono_stack = list()
        n = len(arr)
        for i in range(2 * n - 1, -1, -1):
            while mono_stack and mono_stack[-1] <= arr[i % n]:
                mono_stack.pop()
            result[i % n] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(arr[i % n])
        
        for i, item in enumerate(arr):
            if item is element:
                return result[i]    
         
    return -1

def power(x, y):
    result = 1.0
    if y < 0:
        x, y = 1.0 / x, -y
        
    while y:
        if y & 1:
            result *= x
        x, y = x * x, y >> 1
    
    return result


# Utility function to segregate array such that even numbers appear before than odds
def even_odd_segregation(num_array):
    if num_array:
        low, high = 0, len(num_array) - 1
        while low < high:
            if num_array[low] % 2 == 0:
                low += 1
            else:
                num_array[low], num_array[high] = num_array[high], num_array[low]
                high -= 1


# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
def valid_palindrome(s):
    if s:

        def valid_palindrome(low, high, num_missed_allowed=1):
            while low < high:
                if s[low] != s[high]:
                    if num_missed_allowed > 0:
                        if (s[low + 1] == s[high] and 
                                s[low] == s[high - 1]):
                            return any([valid_palindrome(low + 1, high, 0), valid_palindrome(low, high - 1, 0)])
                        elif s[low + 1] == s[high]:
                            low += 1
                            num_missed_allowed -= 1
                        elif s[low] == s[high - 1]:
                            high -= 1
                            num_missed_allowed -= 1
                        else:
                            return False
                    else:
                        return False
                else:
                    low += 1
                    high -= 1
            
            return True
        
        return valid_palindrome(0, len(s) - 1)

from string import digits

def base_neg_2(n):
    def modified_divmod(num, base):
        result = dict()
        if (num, base) not in result:
            div, mod = divmod(num, base)
            if mod < 0:
                temp = (div * base) + base
                div, mod = temp // base, num - temp
            result[(num, base)] = (div, mod)
        return result[(num, base)]
    
    def construct_from_base(decimal_number, base):
        return ('' if decimal_number == 0 else 
                    construct_from_base(modified_divmod(decimal_number, base)[0], base) + 
                        digits[modified_divmod(decimal_number, base)[1]]) 

    return '0' if n == 0 else construct_from_base(n, -2)

def n_queens_prac_2(n):

    def queens_placement_helper(row):
        if row == n:
            result.append(copy(queens_placement))
        else:
            for col in range(n):
                if all(abs(col - queens_placement[i]) not in (row - i, 0) 
                       for i in range(len(queens_placement[:row]))):
                    queens_placement[row] = col
                    queens_placement_helper(row + 1)

    result = list()
    queens_placement = [0] * n
    queens_placement_helper(0)
    return result

def knapsack_without_repetition_prac_2(items, max_weight):
    if items:
        ans = [[0] * (max_weight + 1) for _ in range(len(items) + 1)]
        for i in range(1, len(items) + 1):
            for j in range(1, max_weight + 1):
                if items[i - 1].weight > j:
                    ans[i][j] = ans[i - 1][j]
                else:
                    ans[i][j] = max(
                            ans[i - 1][j],
                            ans[i - 1][j - items[i - 1].weight] + items[i - 1].value
                        )
        
        return ans[len(items)][max_weight]
    return 0

def is_match(text, pattern):
    registry = dict()
    
    def regex_helper(i, j):
        if (i, j) not in registry:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in ('.', text[i])
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = regex_helper(i, j+2) or first_match and regex_helper(i+1, j)
                else:
                    ans = regex_helper(i+1, j+1)
            registry[i, j] = ans
        return registry[i, j]
        
    return regex_helper(0, 0)
    
if __name__ == '__main__':
    # print n_queens(4)
    
    # items = [Item(6, 30), Item(3, 14), Item(4, 16), Item(2, 9)]
    # print knapsack_with_repetition(items, 10)
    # print knapsack_without_repetition(items, 10)
    # print knapsack_without_repetition_prac_2(items, 10)
    
    # grid = [
    #   ["1","1","0","0","0"],
    #   ["1","1","0","0","0"],
    #   ["0","0","1","0","0"],
    #   ["0","0","0","1","1"]
    # ]
    
    # grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    # pprint(grid, width=32)
    # print numIslands(grid)
    
    # print levensthein_distance('polynomial', 'exponential')
    
    # arr = [10, 3, 4, 6, 9]
    # print find_next_greater_element(arr, 9) 
    # print find_next_greater_element_in_circular_array(arr, 9)
    # print n_queens_prac_2(4) 
    
    print is_match('aab', 'c*a*b')
    
    # print power(2, -20)
    
    # num_array = [2, 3, 5, 8, 9, 11, 13, 17]
    # even_odd_segregation(num_array)
    # print num_array
    
    # print valid_palindrome('aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga')
    # print valid_palindrome("pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip")
    
    print base_neg_2(0)
    print base_neg_2(2)
    print base_neg_2(3)
    print base_neg_2(4)



