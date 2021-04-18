from pprint import pprint


def find_longest_common_subsequence(text1, text2):
    if text1 and text2:
        result = [[0] * len(text2) for _ in range(len(text1))]
        for i, c1 in enumerate(text1):
            for j, c2 in enumerate(text2):
                if c1 == c2:
                    result[i][j] = 1 + (result[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0)
                else:
                    result[i][j] = max(result[i-1][j], result[i][j-1])
        pprint(result, width=32)
        return result[len(text1)-1][len(text2)-1]


if __name__ == '__main__':
    print find_longest_common_subsequence('fish', 'fosh')
    print find_longest_common_subsequence('fort', 'fosh')
    print find_longest_common_subsequence('microsoft', 'cross')
    print find_longest_common_subsequence('fifo', 'fosh')
    print find_longest_common_subsequence('ufo', 'surround')
