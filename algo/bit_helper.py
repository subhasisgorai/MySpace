def get_bit(number, i):
    return 1 if number & 1 << i else 0


def set_bit(number, i):
    return number | 1 << i


def clear_bit(number, i):
    return  number & ~(1 << i)


def clear_bits_msb_to_ith(number, i):
    return number & ((1 << i) - 1)


def clear_bits_i_thru_0(number, i):
    return number & ~((1 << (i + 1)) - 1)


if __name__ == '__main__':
    print get_bit(0b110111, 3)
    print bin(set_bit(0b110111, 3))
    print bin(clear_bit(0b110111, 2))
    print bin(clear_bits_msb_to_ith(0b1101110, 2))
    print bin(clear_bits_i_thru_0(0b1101110, 3))
