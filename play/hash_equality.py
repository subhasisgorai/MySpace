# interesting article https://hynek.me/articles/hashes-and-equality/


class C:

    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return 'C({})'.format(self.x)

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.x == other.x
        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)
    

if __name__ == '__main__':
    d = dict()
    s = set()
    
    c = C(1)
    d[c] = 42
    s.add(c)
    
    print d, s
    print c in s and c in d
    
    c.x = 2
    print c
    
    print c in s or c in d
    print d, s
    
    print C(1) in s or C(1) in d
