from pprint import pprint


def find_longest_common_substring(str1, str2):
    if str1 and str2:
        result = [[0 for _ in range(len(str2))] for i in range(len(str1))]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    result[i][j] = 1 + (result[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0)
        pprint(result, width=32)
        return find_max_in_the_grid(result)
    return 0


def find_max_in_the_grid(data):
    if data:
        max_num = 0
        for i in range(len(data)):
            inner_array = data[i]
            for j in range(len(inner_array)):
                max_num = max(max_num, data[i][j])
        return max_num


if __name__ == '__main__':
    print find_longest_common_substring('fish', 'fosh')
    print find_longest_common_substring('fort', 'fosh')
    print find_longest_common_substring('microsoft', 'cross')
