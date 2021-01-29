from pprint import pprint


def find_longest_common_subsequence(str1, str2):
    if str1 and str2:
        result = [[0 for _ in range(len(str2))] for i in range(len(str1))]
        for i in range(len(str1)):
            for j in range(len(str2)):
                result[i][j] = (1 if str1[i] == str2[j] else 0) + max(result[i - 1][j] if i - 1 >= 0 else 0,
                                                                    result[i][j - 1] if j - 1 >= 0 else 0)
        pprint(result, width=32)
        return result[len(str1) - 1][len(str2) - 1]
        
    return 0


if __name__ == '__main__':
    print find_longest_common_subsequence('fish', 'fosh')
    print find_longest_common_subsequence('fort', 'fosh')
    print find_longest_common_subsequence('microsoft', 'cross')
    print find_longest_common_subsequence('fifo', 'fosh')
    print find_longest_common_subsequence('ufo', 'surround')
