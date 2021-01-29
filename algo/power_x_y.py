def power(x, y):
    result = 1.0
    count = 0
    while y:
        result *= x 
        y -= 1
        count += 1
        
    print count
    return result


# Exponentiation by Squaring
def power_improved(x, y):
    result, power, count = 1.0, y, 0
    if y < 0:
        x, power = 1.0 / x, -power 
    while power:
        if power & 0b1:
            result *= x
        x, power, count = x * x, power >> 1, count + 1  
         
    print count
    return result


if __name__ == '__main__':
    print power(12, 100)
    print power_improved(12, 100)
    print power(1.1, 20)
    print power_improved(1.1, 20)
