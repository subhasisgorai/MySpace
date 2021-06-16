
def find_nearest_Palindrome(n):
    def assertValidInteger(sample):
        assert (sample is not None and
                    sample >= 0 and 
                    isinstance(sample, int)), 'number should be a not null valid positive integer'
        
    assertValidInteger(int(n))
    
    # some useful inner functions
    def convert_num_to_array(number):
        return map(int, number)
    
    def check_all_digits_nine(num_arr):
        return all(i == 9 for i in num_arr)
    
    def check_all_digits_zero(num_arr):
        return all(i == 0 for i in num_arr)
    
    def reverse_array(array):
        return array[::-1]
    
    def get_back_the_number(left_arr, mid_arr, right_arr):
        resultant_array = map(str, left_arr + mid_arr + right_arr)
        return int(reduce(lambda a, b: a + b, resultant_array))
    
    def is_even(number):
        return True if number and number % 2 == 0 else False
    
    def get_initial_palindrome(num_arr):
        num_len = len(num_arr)
        left_arr, mid_arr = list(), list()

        counter = 0
        mid = (num_len - 1) // 2
        while(counter < mid):
            left_arr.append(num_arr[counter])
            counter += 1

        if is_even(num_len):
            mid_arr.append(num_arr[mid])
            mid_arr.append(num_arr[mid])
        else:
            mid_arr.append(num_arr[mid])

        right_arr = reverse_array(left_arr)

        return (get_back_the_number(left_arr, mid_arr, right_arr), left_arr, mid_arr, right_arr)
    
    def get_prev_palindrome(num_arr):
        initial_palindrome, left_arr, mid_arr, right_arr = get_initial_palindrome(num_arr)
        
        if initial_palindrome >= int(n):
            mid_arr = list(map(lambda i: i - 1 if i > 0 else 9, mid_arr))
            if mid_arr[0] == 9:
                curr_pos, carry = len(left_arr) - 1, 1
                while curr_pos >= 0 and carry > 0:
                    left_arr[curr_pos], carry = (left_arr[curr_pos] - carry, 0) if left_arr[curr_pos] > 0 else (9, 1)
                    curr_pos -= 1
                right_arr = reverse_array(left_arr)
            final_palindrome = get_back_the_number(left_arr, mid_arr, right_arr)
        else:
            final_palindrome = initial_palindrome
            
        return final_palindrome
    
    def get_next_palindrome(num_arr):
        initial_palindrome, left_arr, mid_arr, right_arr = get_initial_palindrome(num_arr)

        if initial_palindrome <= int(n):
            mid_arr = list(map(lambda i: i + 1 if i < 9 else 0, mid_arr))
            if mid_arr[0] == 0:
                curr_pos, carry = len(left_arr) - 1, 1
                while curr_pos >= 0 and carry > 0: 
                    new_val = left_arr[curr_pos] + carry
                    left_arr[curr_pos], carry = (new_val, 0) if new_val < 10 else (0, 1)
                    curr_pos -= 1
                right_arr = reverse_array(left_arr)
            final_palindrome = get_back_the_number(left_arr, mid_arr, right_arr)
        else:
            final_palindrome = initial_palindrome
            
        return final_palindrome
    
    # actual implementation starts here
    num_arr = list(convert_num_to_array(n))
    if num_arr:
        if len(num_arr) == 1:
            return str(int(n) - 1) if int(n) >= 1 else str(int(n) + 1)
            
        if check_all_digits_nine(num_arr):
            return str(int(n) + 2)
        
        if num_arr[0] == 1 and check_all_digits_zero(num_arr[1:-1]) and num_arr[-1] in (0, 1):
            return reduce(lambda a,b : a+b, ['9' for _ in range(len(num_arr)-1)])

        next_palindrome = get_next_palindrome(num_arr)
        prev_palindrome = get_prev_palindrome(num_arr)

        return str(next_palindrome 
                    if abs(next_palindrome - int(n)) < abs(int(n) - prev_palindrome)
                    else prev_palindrome)

if __name__ == '__main__':
    print find_nearest_Palindrome('123')
    print find_nearest_Palindrome('1')
    print find_nearest_Palindrome('10')
