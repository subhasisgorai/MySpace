def intersect_sorted_arrays(arr_1, arr_2):
    result = list()
    if arr_1 and arr_2:
        i, j = 0, 0
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] == arr_2[j]:
                if i == 0 or arr_1[i - 1] != arr_1[i]:
                    result.append(arr_1[i])
                i, j = i + 1, j + 1
            elif arr_1[i] < arr_2[j]:
                i += 1
            else:
                j += 1
    return result


if __name__ == '__main__':
    arr_1 = [1, 2, 2, 3, 3, 3, 3, 7, 7, 8, 9]
    arr_2 = [0, 2, 3, 3, 3, 5, 6, 7, 8, 9, 15]
    print intersect_sorted_arrays(arr_1, arr_2)
