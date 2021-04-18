def plusOne(digits):

    def add_helper(digit):
        plus_one = digit + 1
        return (0, 1) if plus_one == 10 else (plus_one, 0)
    
    if digits:
        digits.reverse()
        carry = 0
        for i, digit in enumerate(digits):
            if i == 0 or carry > 0:
                digits[i], carry = add_helper(digit)
            else:
                break
        if carry == 1:
            digits.append(1)
        
        digits.reverse()
        return digits
    
if __name__ == '__main__':
    print plusOne([1,2,3])
    print plusOne([4,3,2,1])
    print plusOne([0])
    print plusOne([999])
