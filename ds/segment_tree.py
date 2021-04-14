from collections import namedtuple

Node = namedtuple('Node', ('a', 'b', 'max_value'))

'''
    Segment trees are very fast for searching over an interval.
    A segment tree is a binary tree where leaf nodes store the original data,
    internal nodes store information about the segment of that data.
    The construction of the tree takes O(n * log n) time while searching 
    takes O(log n).
    
    Here is a Segment Tree for the purpose of efficient queries to find the
    maximum item in a range provided
'''


class SegmentTree:

    def __init__(self, vector):
        self.form_segment_tree(vector)
        
    def form_segment_tree(self, vector):
        # let's find out the size of the tree
        n = 1
        while n < len(vector):
            n *= 2
        
        segment_tree = [0] * (2 * n - 1)
        
        # assign the original data to the leaf nodes, add necessary
        # nodes to make a full binary tree, without affecting the result
        j = 0
        for i in range(n - 1, 2 * n - 1):
            segment_tree[i] = (Node(j, j, vector[j]) if j < len(vector) 
                                    else Node(j, j, 0))
            j += 1
        
        # compute the internal nodes starting from the leaf nodes to root
        for i in range(2 * n - 2, 0, -2):
            a = segment_tree[i - 1].a
            b = segment_tree[i].b
            max_value = max(segment_tree[i - 1].max_value,
                            segment_tree[i].max_value)
            segment_tree[(i - 1) // 2] = Node(a, b, max_value)
         
        self.segment_tree = segment_tree

    def find_max_value_in_range(self, a, b, k):
        if (b < self.segment_tree[k].a or
                    a > self.segment_tree[k].b):
            return 0
        
        a = max(a, self.segment_tree[k].a)
        b = min(b, self.segment_tree[k].b)
        
        if (a == self.segment_tree[k].a and
                    b == self.segment_tree[k].b):
            return  self.segment_tree[k].max_value
        
        return max(self.find_max_value_in_range(a, b, 2 * k + 1),
                        self.find_max_value_in_range(a, b, 2 * k + 2))
        
    def get_max_value(self, a, b):
        return self.find_max_value_in_range(a, b, 0)

    
if __name__ == '__main__':
    arr = [5, 3, 8, 1, 5, 7, 4, 0, 9, 2, 6]
    print 'The given vector: {}\n'.format(arr)
    st = SegmentTree(arr)
    print 'In range ({}, {}), maximum value: {}'.format(2, 5, st.get_max_value(2, 5))
    print 'In range ({}, {}), maximum value: {}'.format(3, 9, st.get_max_value(3, 9))
    print 'In range ({}, {}), maximum value: {}'.format(2, 3, st.get_max_value(2, 3))
    print 'In range ({}, {}), maximum value: {}'.format(4, 7, st.get_max_value(4, 7))
    print 'In range ({}, {}), maximum value: {}'.format(9, 10, st.get_max_value(9, 10))
    print 'In range ({}, {}), maximum value: {}'.format(0, 0, st.get_max_value(0, 0))
    print 'In range ({}, {}), maximum value: {}'.format(10, 10, st.get_max_value(10, 10))
    print 'In range ({}, {}), maximum value: {}'.format(0, 10, st.get_max_value(0, 10))
    
