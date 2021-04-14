class PriorityQueueBase:

    class _Item:
        __slots__ = '_key', '_value'
        
        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            if self.__class__ == other.__class__:
                return self._key < other._key
            return NotImplemented
    
    def is_empty(self):
        return len(self) == 0
    
''' A min-heap implementation with a binary heap
'''
class HeapPriorityQueue(PriorityQueueBase):

    def _parent(self, j):
        return (j - 1) // 2
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)
            
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)
    
    def __init__(self):
        self._data = list()
        
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)
    
    def min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        item = self._data[0]
        return  (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
        
    def items(self):
        while not self.is_empty():
            yield self.remove_min()


if __name__ == '__main__':
    heap = HeapPriorityQueue()
    print 'adding (5, 4) to heap' 
    heap.add(5, 4)
    
    print 'adding (10, 7) to heap'
    heap.add(10, 7)
    
    print 'adding (11, 3) to heap'
    heap.add(11, 3)
    
    a_tuple = (3, 3)
    print 'adding {} to heap'.format(a_tuple)
    heap.add(*a_tuple)
    
    print 'adding (19, 23) to heap'
    heap.add(19, 23)
    
    print 'adding (25, 11) to heap'
    heap.add(25, 11)
    
    print 'now removing the items added'
    for item in heap.items():
        print item,
    
