

def next_greater_element(n):

    def get_digits_array(num):
        return map(int, str(num))
    
    def get_number_from_digits(digits_arr):
        digits_arr = map(str, digits_arr)
        return int(reduce(lambda a, b: a + b, digits_arr))

    if n > 0:
        digits = get_digits_array(n)
        i = len(digits) - 2
        while digits[i] >= digits[i + 1] and i >= 0:
            i -= 1
        if i >= 0:
            for j in range(i + 1, len(digits)):
                if digits[j] <= digits[i]:
                    j -= 1
                    break
            digits[i], digits[j] = digits[j], digits[i]
            new_digits = digits[:i + 1] + list(sorted(digits[i + 1:]))
            new_n = get_number_from_digits(new_digits)
            if new_n > n and new_n <= (2**31 - 1):
                return new_n
            
    return -1


if __name__ == '__main__':
    # print next_greater_element(12)
    # print next_greater_element(21)
    # print next_greater_element(0)
    # print next_greater_element(2147483476)
    # print next_greater_element(12222333)
    print next_greater_element(12443322)


