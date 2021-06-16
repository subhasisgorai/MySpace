
def reverse_words(s):
    def reverse_range(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    s = s.strip()
    s, write_idx = list(s), 0
    
    for i, c in enumerate(s):
        if  c == ' ' and i > 0 and s[i-1] == ' ':
            continue
        s[write_idx] = c
        write_idx += 1
               
    reverse_range(0, write_idx - 1)
    
    start = end = 0
    
    while end < write_idx:
        while end < write_idx and s[end] != ' ':
            end += 1
        reverse_range(start, end-1)
        end = end + 1
        start =  end
        
    new_sentence = s[:write_idx]
    return ''.join(new_sentence)
        
if __name__  == '__main__':
    print reverse_words('      Hello       World  ')
    print reverse_words('')
    