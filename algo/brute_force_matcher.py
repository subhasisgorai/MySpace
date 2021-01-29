

def find_brute_force(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        k = 0
        while k < m and text[i + k] == pattern[k]:
            k += 1
        if k == m:
            return i
    return -1

        
text = 'subhasis'
pattern = 'ubhas'

print find_brute_force(text, pattern)
