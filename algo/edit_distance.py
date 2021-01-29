

def find_edit_distance(str1, str2):
    assert str1, 'str1 should be a valid non empty string'
    assert str2, 'str2 should be a valid non empty string'
    if str1 == str2:
        return 0
    else:
        edits = [[0 for _ in range(0, len(str1) + 1)] for i in range(0, len(str2) + 1)]
        for j in range(1, len(str1) + 1):
            edits[0][j] = j
        for i in range(1, len(str2) + 1):
            edits[i][0] = i
            
        for i in range(1, len(str2) + 1):
            for j in range(1, len(str1) + 1):
                edits[i][j] = min(edits[i - 1][j] + 1, edits[i][j - 1] + 1,
                                    edits[i - 1][j - 1] + (0 if str2[i - 1] == str1[j - 1] else 1))
        
        return edits[i][j]

        
if __name__ == '__main__':
    print find_edit_distance('POLYNOMIAL', 'EXPONENTIAL')
    print find_edit_distance('SUNNY', 'SNOWY')
    print find_edit_distance('ZEBRA', 'ZEBIA')
    print find_edit_distance('ZEBRA', 'ABHRA')
