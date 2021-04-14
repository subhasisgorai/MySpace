from timeit import repeat

def count_bits(number):
    result = 0 
    while number:
        result += number & 1
        number >>= 1
    return result


def count_bits_better(number):
    result = 0
    while number:
        number &= number - 1
        result += 1
    return result


if __name__ == '__main__':
    print count_bits(0b11011010101)
    print count_bits(0b11111111)
    print count_bits(0b00000000)
    
    print count_bits_better(0b11011010101)
    print count_bits_better(0b11111111)
    print count_bits_better(0b00000000)

    print repeat(stmt='count_bits(0b11011010101)', setup='from bit_counter import count_bits', number=1000000, repeat=3)
    print repeat(stmt='count_bits_better(0b11011010101)', setup='from bit_counter import count_bits_better', number=1000000, repeat=3)