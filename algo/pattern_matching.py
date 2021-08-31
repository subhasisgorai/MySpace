from timeit import repeat


# The worst-case running time of the brute-force method is O(nm)
def brute_force(text, pattern):
    if text and pattern:
        n, m = len(text), len(pattern)
        for i in range(n - m + 1):
            for k in range(m):
                if text[i + k] != pattern[k]:
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


from functools import reduce 


def rabin_karp(text, pattern):

    def confirm_equal(str1, hash_1, str2, hash_2):
        return hash_1 == hash_2 and str1 == str2 
        
    len_t, len_p = len(text), len(pattern)
    if len_p > len_t:
        return -1
    
    base = 26
    hash_t = reduce(
                lambda rs, c: base * rs + ord(c),
                    text[:len_p], 0)
    hash_p = reduce(
                lambda rs, c: base * rs + ord(c),
                    pattern, 0)
    power_max = base ** max(len_p - 1, 0)
    
    for i in range(len_p, len_t):
        if confirm_equal(text[i - len_p:i], hash_t, pattern, hash_p):
            return i - len_p
        hash_t -= ord(text[i - len_p]) * power_max
        hash_t = hash_t * base + ord(text[i])
    
    if confirm_equal(text[-len_p:], hash_t, pattern, hash_p):
        return len_t - len_p
    return -1


if __name__ == '__main__':
    print brute_force('Hello World', 'lo Wo')
    print brute_force('Hello World', 'lo wo')
    
    print boyer_moore('Hello World', 'lo Wo')
    print boyer_moore('Hello World', 'lo wo')
    
    print rabin_karp('Hello World', 'lo Wo')
    print rabin_karp('Hello World', 'lo wo')
    
    
    print repeat('brute_force(\'Hello World\', \'lo Wo\')', 'from algo.pattern_matching import brute_force', repeat=3)
    print repeat('boyer_moore(\'Hello World\', \'lo Wo\')', 'from algo.pattern_matching import boyer_moore', repeat=3)
    print repeat('rabin_karp(\'Hello World\', \'lo Wo\')', 'from algo.pattern_matching import rabin_karp', repeat=3)                
