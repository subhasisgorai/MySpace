from heappq import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue): 

    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'
    
        def __init__(self, key, value, index):
            super(AdaptableHeapPriorityQueue.Locator, self).__init__(key, value)
            self._index = index
            
        def __str__(self):
            return '[key: {}, value: {}, index: {}]'.format(self._key, self._value, self._index)
        
        def __repr__(self):
            return self.__str__()
            
    def _swap(self, i, j):
        super(AdaptableHeapPriorityQueue, self)._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j
    
    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)
            
    def add(self, key, value):
        token = AdaptableHeapPriorityQueue.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token
    
    def update(self, loc, new_key, new_value):
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        loc._key, loc._value = new_key, new_value
        self._bubble(j)
        
    def remove(self, loc):
        j = loc._index
        if not (0 < j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        if len(self._data) - 1 == j:
            self._data.pop()
        else:
            self.swap(j, len(self) - 1)
            self._data.pop()
            self._bubble(j)
        return (loc._key, loc._value)

     
if __name__ == '__main__':
    q = AdaptableHeapPriorityQueue()
    q.add(5, 'test_5') 
    q.add(3, 'test_3') 
    q.add(2, 'test_2')
    q.add(10, 'test_10')
    
    print q.remove_min()
    
    q.add(1, 'test_1')
    loc_8 = q.add(8, 'test_8')
    q.add(4, 'test_4')
    
    print q.min()
