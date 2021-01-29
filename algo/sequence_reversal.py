

def reverse(sequence, start, stop):
    if start < stop:
        sequence[start], sequence[stop] = sequence[stop], sequence[start]
        reverse(sequence, start + 1, stop - 1) 


sequence = [1, 2, 3, 4, 5, 6, 7]
reverse(sequence, 0, len(sequence) - 1)

print sequence
