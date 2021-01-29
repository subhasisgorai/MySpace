def count_bits(number):
    result = 0 
    while number:
        result += number & 1
        number >>= 1
    return result

        
if __name__ == '__main__':
    print count_bits(0b11011010101)
    print count_bits(0b11111111)
    print count_bits(0b00000000)
