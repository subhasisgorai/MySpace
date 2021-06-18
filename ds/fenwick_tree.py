'''
    A Fenwick tree is most easily understood by considering a one-based array. Each element 
    whose index i is a power of 2 contains the sum of the first i elements. Elements whose indices 
    are the sum of two (distinct) powers of 2 contain the sum of the elements since the preceding power of 2. 
    In general, each element contains the sum of the values since its parent in the tree, and 
    that parent is found by clearing the least-significant bit in the index.
    To find the sum up to any given index, consider the binary expansion of the index, and add elements 
    which correspond to each 1 bit in the binary form.
'''


class FenwickTree:

    def __init__(self, vector):
        self.vector = vector
        self.input_size = len(vector)
        self.fenwick_tree = [0] * (self.input_size + 1)
        
    def form_tree(self):
        for i in range(self.input_size):
            self.update_tree(i, self.vector[i])
            
    def update_tree(self, i, v):
        i += 1
        while i <= self.input_size:
            self.fenwick_tree[i] += v
            i += (i & -i)
            
    def prefix_sum(self, i):
        res = 0
        i += 1
        while i > 0:
            res += self.fenwick_tree[i]
            i -= (i & -i)
        return res
    
    def query(self, i , j):
        return self.prefix_sum(j) - self.prefix_sum(i - 1)
            
    def __str__(self):
        return str(self.fenwick_tree)

            
if __name__ == '__main__':
    input_arr = [1, 4, 2, 4, 3, 0, 7, 5, 1, 6]
#   input_arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print 'Input array: {}'.format(input_arr)
    
    ft = FenwickTree(input_arr)
    ft.form_tree()
    print 'Fenwick Tree formed: {}'.format(ft)
    
    print 'Sum for range [2, 5]: {}'.format(ft.query(2, 5))
    
