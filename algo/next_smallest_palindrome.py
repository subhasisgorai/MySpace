

def find_brute_force(number):
    __assertValidInteger(number)
    temp = number + 1
    while(not is_palindrome(temp)):
        temp += 1
    return temp


def find_optimized_manner(number):
    __assertValidInteger(number)
    num_arr = __convert_num_to_array(number)
    if num_arr:
        if __check_all_digits_nine(num_arr):
            return number + 2 
        
        num_len = len(num_arr)
        left_arr, mid_arr, right_arr = list(), list(), list()
        
        counter = 0
        mid = (num_len - 1) / 2
        while(counter < mid):
            left_arr.append(num_arr[counter])
            counter += 1
            
        if __is_even(num_len):
            mid_arr.append(num_arr[mid])
            mid_arr.append(num_arr[mid])
            counter += 2
        else:
            mid_arr.append(num_arr[mid])
            counter += 1
            
        right_arr = __reverse_array(left_arr)
        
        initial_palindrome = __get_back_the_number(left_arr, mid_arr, right_arr)
        
        if initial_palindrome <= number:
            mid_arr = map(lambda i: i + 1 if i < 9 else 0, mid_arr)
            if mid_arr[0] == 0:
                curr_pos = len(left_arr) - 1
                carry = 1
                while curr_pos >= 0 and carry > 0: 
                    new_val = left_arr[curr_pos] + carry
                    left_arr[curr_pos], carry = (new_val, 0) if new_val < 10 else (0, 1)
                    curr_pos -= 1
                right_arr = __reverse_array(left_arr)
                
            final_palindrome = __get_back_the_number(left_arr, mid_arr, right_arr)
        else:
            final_palindrome = initial_palindrome
        
        return final_palindrome
        

def is_palindrome(number):
    __assertValidInteger(number)
    number_str = str(number)
    reveresed_str = number_str[::-1]
    return number_str == reveresed_str


def __check_all_digits_nine(num_arr):
    if num_arr:
        for i in num_arr:
            if i != 9:
                return False
        return True
    else:
        return False


def __get_back_the_number(left_arr, mid_arr, right_arr):
    resultant_array = list()
    
    if left_arr: resultant_array.extend(left_arr) 
    if mid_arr: resultant_array.extend(mid_arr) 
    if right_arr: resultant_array.extend(right_arr)
    
    resultant_array = map(str, resultant_array)
    return int(reduce(lambda a, b: a + b, resultant_array)) 


def __reverse_array(array):
    if array:
        return array[::-1]

        
def __is_even(number):
    return True if number and number % 2 == 0 else False


def __convert_num_to_array(number):
    return map(int, str(number))


def __assertValidInteger(sample):
    assert (sample is not None and
                sample >= 0 and 
                isinstance(sample, int)), 'number should be a not null valid positive integer' 
