from  string import hexdigits


def convert_base(num_as_str, b1, b2): 

    def construct_from_base(num, base):
        return ('0' if num == 0 else 
                (construct_from_base(num // base, base) 
                    if num // base > 0 else '') + 
                hexdigits[num % base].upper())
    
    is_negative = num_as_str[0] == '-'
    num_base_10 = reduce(lambda a, b: a * b1 + hexdigits.index(b.lower()),
                         num_as_str[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if  num_base_10 == 0  else
                                           construct_from_base(num_base_10, b2))


if __name__ == '__main__': 
    print convert_base('111011', 2, 16) 
