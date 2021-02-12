
'''
    When Disjoint Partitions and Union-Find Structures implemented
    using Union-by-size and Path Compression heuristics, 
    a series of k operations involving n elements takes O(klog*n) time.
        where, log*n is log-star function which is the inverse of tower-of-twos
            function[tetration]. Intuitively, log*n is the number of times one can 
            iteratively take the logarithm (base 2) of a number before getting a number smaller 
            than 2.
'''


class Partition:

    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'
        
        def __init__(self, container, element):
            self._container = container  # reference to Partition instance
            self._element = element
            self._size = 1
            self._parent = self  # initial group leader
            
        def element(self):
            return self._element
    
    def make_group(self, element):
        return self.Position(self, element)
    
    def find(self, p):
        if p._parent != p:
            p._parent = self.find(
                        p._parent  # Path compression, update _parent after recursion
                    ) 
        return p._parent
    
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            # union-by-size implementation
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
        
