

class TreeNode:

    def __init__(self, low, high, range_sum):
        self.low, self.high, self.range_sum = low, high, range_sum


class SegmentTree:

    def __init__(self, vector):
        self.form_segment_tree(vector)
        
    def form_segment_tree(self, vector):
        n, j = 1, 0
        while n < len(vector):
            n *= 2
        segment_tree = [0] * (2 * n - 1)
        
        # let's fill the leaf nodes first
        for i in range(n - 1, 2 * n - 1):
            segment_tree[i] = (TreeNode(j, j, vector[j]) if j < len(vector) 
                               else TreeNode(j, j, 0))
            j += 1
            
        # time for populating the internal nodes as well
        for i in range(2 * n - 2, 0, -2):
            low = segment_tree[i - 1].low
            high = segment_tree[i].high
            summation = segment_tree[i - 1].range_sum + segment_tree[i].range_sum
            segment_tree[(i - 1) // 2] = TreeNode(low, high, summation)
            
        self.segment_tree = segment_tree
        self.n = n
        
    def _find_sum_range(self, low, high, k):
        if high < self.segment_tree[k].low or low > self.segment_tree[k].high:
            return 0
        
        low = max(low, self.segment_tree[k].low)
        high = min(high, self.segment_tree[k].high)
        
        if self.segment_tree[k].low == low and self.segment_tree[k].high == high:
            return self.segment_tree[k].range_sum
        
        return (self._find_sum_range(low, high, 2 * k + 1) + 
                    self._find_sum_range(low, high, 2 * k + 2))
        
    def get_sum_range(self, low, high):
        return self._find_sum_range(low, high, 0)
                
    def update_node(self, index, new_val):
        index += self.n - 1
        delta = new_val - self.segment_tree[index].range_sum   
        while index >= 0:
            self.segment_tree[index].range_sum += delta
            index = (index - 1) // 2

            
if __name__ == '__main__':
    arr = [5, 3, 8, 1, 5, 7, 4, 0, 9, 2, 6]
    print 'The given vector: {}\n'.format(arr)
    st = SegmentTree(arr)
    print 'In range ({}, {}), the summation value: {}'.format(2, 5, st.get_sum_range(2, 5))
    st.update_node(4, 8)
    print 'In range ({}, {}), the summation value: {}'.format(2, 5, st.get_sum_range(2, 5))
