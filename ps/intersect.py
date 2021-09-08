

def intersection(l1, l2):
    if l1 and l2:
        first_set, result = set(l1), list()
        for item in l2:
            if item in first_set:
                result.append(item)
        return result        
    return []

if __name__ == '__main__':
    print intersection(['foo', 'bar', 'baz'], 
                       ['baz', 'biz', 'boo'])