class PriorityQueueBase(object):

    class _Item(object):
        __slots__ = '_key', '_value'
        
        def __init__(self, key, value):
            self._key = key
            self._value = value
            
        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):

    # --- non-public behaviors
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def has_left(self, j):
        return self._left(j) < len(self._data)
    
    def has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        storage = self._data
        storage[i], storage[j] = storage[j], storage[i]
        
    def _upheap(self, j):
        parent = self._parent(j)
        if parent >= 0 and self._data[parent] > self._data[j]:
            self._swap(j, parent)
            self._upheap(parent)
            
    def _downheap(self, j):
        if self.has_left(j):
            left_child = self._left(j)
            smaller_child = left_child
            if self.has_right(j):
                right_child = self._right(j)
                if self._data[right_child] < self._data[left_child]:
                    smaller_child = right_child
            if self._data[smaller_child] < self._data[j]:
                    self._swap(smaller_child, j)
                    self._downheap(smaller_child)
        
    # --- public behaviors
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
        return item._key, item._value
    
    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority Queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return item._key, item._value

    
if __name__ == '__main__':
    heappq = HeapPriorityQueue()
    heappq.add(5, 'test_5') 
    heappq.add(3, 'test_3') 
    heappq.add(2, 'test_2')
    
    print heappq.remove_min()
    
    heappq.add(1, 'test_1')
    heappq.add(8, 'test_8')
    heappq.add(4, 'test_4')
    
    print heappq.min()
