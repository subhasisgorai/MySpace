import heapq

class Partition:

    class Position:
        __slots__ = '_element', '_parent', '_container', '_size'

        def __init__(self, container, element):
            self._container = container
            self._element = element
            self._parent = self
            self._size = 1
        
        def element(self):
            return self._element
        
        def container(self):
            return self._container
        
        def __str__(self):
            return 'element: {}, parent: {}'.format(self._element, self._parent) 
        
        def __repr__(self):
            return self.__str__()
    
    def __init__(self):
        self.num_groups = 0
    
    def make_group(self, element):
        self.num_groups += 1
        return Partition.Position(self, element)
    
    def find(self, p):
        if p != p._parent:
            p._parent = self.find(p._parent)
        return p._parent
    
    def union(self, p, q):
        a = self.find(p)
        b = self.find(q)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
            self.num_groups -= 1
    
    def __len__(self):
        return self.num_groups


class Solution:

    def minimumCost(self, N, connections):
        if N > 0 and connections:
            if len(connections) < N - 1:
                return -1
            
            partition = Partition()
            positions_dict = dict()
            spanning_tree = list()
            min_heap = list()
            
            for connection in connections:
                if connection and len(connection) == 3:
                    positions_dict[connection[0]] = partition.make_group(connection[0])
                    positions_dict[connection[1]] = partition.make_group(connection[1])
                    heapq.heappush(min_heap, (connection[2], connection))
                    
            while min_heap and len(spanning_tree) != N - 1:
                connection = heapq.heappop(min_heap)
                u, v = connection[1][0], connection[1][1]
                a, b = partition.find(positions_dict[u]), partition.find(positions_dict[v])
                
                if a is not b:
                    partition.union(a, b)
                    spanning_tree.append(connection[1][2])
            
            return sum(spanning_tree)
            
        return -1
    
if __name__ == '__main__':
    soln = Solution()
    print(soln.minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]]))
