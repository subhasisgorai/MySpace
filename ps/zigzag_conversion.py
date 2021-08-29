

def convert(s, num_rows):
    if s and num_rows > 0:
        if num_rows == 1:
            return s
        assignment_pattern = ([i for i in range(0, num_rows - 1)] + 
                                    [i for i in range(num_rows - 1, 0, -1)])
        pattern_length = len(assignment_pattern)
        div, mod = divmod(len(s), pattern_length)
        assignment_arr = assignment_pattern * div + [assignment_pattern[i] for i in range(mod)]
        parts = [[] for _ in range(num_rows)]
        for i, c in enumerate(s):
            parts[assignment_arr[i]].append(c)
        return ''.join(reduce(lambda a1, a2: a1 + a2, parts))
        