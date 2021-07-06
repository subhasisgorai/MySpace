from timeit import repeat

# The worst-case running time of the brute-force method is O(nm)
def brute_force(text, pattern):
    if text and pattern:
        n, m = len(text), len(pattern)
        for i in range(n - m + 1):
            for k in range(m):
                if not text[i + k] == pattern[k]:
                    break
                if k == m - 1:
                    return i
    return -1


def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0: return 0
    last = dict()
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1 


if __name__ == '__main__':
    print brute_force('Hello World', 'lo Wo')
    print brute_force('Hello World', 'lo wo')
    
    print boyer_moore('Hello World', 'lo Wo')
    print boyer_moore('Hello World', 'lo wo')
    
    print repeat('brute_force(\'Hello World\', \'lo Wo\')', 'from algo.pattern_matching import brute_force', repeat=3)
    print repeat('boyer_moore(\'Hello World\', \'lo Wo\')', 'from algo.pattern_matching import boyer_moore', repeat=3)
                    
