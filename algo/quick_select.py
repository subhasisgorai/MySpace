from random import randint


def quick_select_kth_min(arr, k):
    data_len = len(arr) if arr else 0
    assert k in range(1, data_len + 1), "k is not valid for the given data"
    pivot_index = randint(0, data_len - 1)
    pivot = arr[pivot_index]
    
    less_than_pivot = [i for i in arr if i < pivot] 
    equal_to_pivot = [i for i in arr if i == pivot] 
    greater_than_pivot = [i for i in arr if i > pivot] 

    if k <= len(less_than_pivot):
        return quick_select_kth_min(less_than_pivot, k)
    elif k <= len(less_than_pivot) + len(equal_to_pivot):
        return pivot
    else:
        return quick_select_kth_min(greater_than_pivot,
                            k - len(less_than_pivot) - len(equal_to_pivot))

        
def quick_select_kth_max(arr, k):
    if arr and 0 <= k <= len(arr):
        pivot_index = randint(0, len(arr) - 1)
        pivot = arr[pivot_index]
        
        greater_than_pivot = [i for i in arr if i > pivot]
        equal_to_pivot = [i for i in arr if i == pivot]
        lesser_than_pivot = [i for i in arr if i < pivot]
        
        if k <= len(greater_than_pivot):
            return quick_select_kth_max(greater_than_pivot, k)
        elif k <= len(greater_than_pivot) + len(equal_to_pivot):
            return pivot
        else:
            return quick_select_kth_max(lesser_than_pivot,
                                         k - len(greater_than_pivot) - len(equal_to_pivot))


if __name__ == '__main__':
    print quick_select_kth_min([1, 3, 2, 4, 9, 6, 7, 8, 5, 0], 5)
    print quick_select_kth_max([1, 3, 2, 4, 9, 6, 7, 8, 5, 0], 3)
