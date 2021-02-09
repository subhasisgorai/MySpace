

def is_match(text, pattern):
    registry = dict()

    def regex_helper(i, j):
        if (i, j) not in registry:
            if j == len(pattern):
                ans = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in ('.', text[i])
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    ans = regex_helper(i, j + 2) or first_match and regex_helper(i + 1, j)
                else:
                    ans = regex_helper(i + 1, j + 1)
            registry[i, j] = ans
        
        return registry[i, j]
    
    return regex_helper(0, 0)


if __name__ == '__main__':
    print is_match('aab', 'c*a*b')
