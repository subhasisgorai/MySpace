def parity_check_brute_force(number):
    result = 0
    while number:
        result ^= number & 1
        number >>= 1
    return result


def parity_check_improved(number):
    result = 0
    while number:
        result ^= 1
        number &= (number - 1)
    return result


def parity_check_further_improved_64_bits(number):
    number ^= number >> 32
    number ^= number >> 16
    number ^= number >> 8
    number ^= number >> 4
    number ^= number >> 2
    number ^= number >> 1
    number &= 0x1
    
    return number


if __name__ == '__main__':
    print parity_check_brute_force(0b1100111101)
    print parity_check_improved(0b1100111101)
    print parity_check_further_improved_64_bits(0b1100111101)
