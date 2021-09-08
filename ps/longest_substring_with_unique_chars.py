

def find_longest_chars_with_distinct_chars(input_str):
    left_boundary = right_boundary = result = 0
    char_mapping = [-1] * 128
    
    for right_boundary in range(len(input_str)):
        char_at_right_boundary = input_str[right_boundary]
        char_index = char_mapping[ord(char_at_right_boundary)]
        if (char_index != -1 and 
                char_mapping[ord(char_at_right_boundary)] >= left_boundary):
            left_boundary = char_mapping[ord(char_at_right_boundary)] + 1
        result = max(result, right_boundary - left_boundary + 1)
        char_mapping[ord(char_at_right_boundary)] = right_boundary
        right_boundary += 1
    return result


if __name__ == '__main__':
    print find_longest_chars_with_distinct_chars('subhasis')
