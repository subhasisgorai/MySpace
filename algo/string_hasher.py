from functools import reduce


def string_hash(s):
    mult = 997
    return reduce(lambda v, c: v * mult + ord(c), s, 0)


def cyclic_shift_hash(s):
    mask = (1 << 32) - 1
    h = 0
    for c in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(c)
    return h


if __name__ == '__main__':
    print string_hash('Subhasis')
    print string_hash('subhasis')
    print string_hash('Suhbassi')
    print string_hash('abc')
    print string_hash('cba')
    
    print cyclic_shift_hash('Subhasis')
    print cyclic_shift_hash('subhasis')
    print cyclic_shift_hash('Suhbassi')
    print cyclic_shift_hash('abc')
    print cyclic_shift_hash('cba')

