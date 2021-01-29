from timeit import repeat


def bubble_sort(sequence):
    outer_counter = sequencer(len(sequence) - 1, step=-1)
    while True:
        outer = next(outer_counter)
        for i in range(0, outer):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
            i += 1
        if outer == 1:
            break


def selection_sort(sequence):
    i = 1 
    while i < len(sequence) - 1:
        min_num_index = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_num_index]:
                min_num_index = j
            j += 1
        sequence[i - 1], sequence[min_num_index] = sequence[min_num_index], sequence[i - 1]
        i += 1


def insertion_sort(sequence):
    for k in range(1, len(sequence)):
        temp = sequence[k]
        j = k
        while j > 0 and sequence[j - 1] > temp:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = temp
        

def shell_sort(sequence):
    seq_len = len(sequence)
    h = 1
    while h < seq_len / 3:
        h = 3 * h + 1
    while h > 0:
        outer = h
        while outer < seq_len:
            inner = outer
            temp = sequence[outer]
            while inner >= h and sequence[inner - h] > temp:
                sequence[inner] = sequence[inner - h]
                inner -= h
            sequence[inner] = temp 
            outer += 1  
        h = (h - 1) // 3  


def merge_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return
    mid = length // 2
    
    sequence1 = sequence[0:mid]
    sequence2 = sequence[mid:length]
    
    merge_sort(sequence1)   
    merge_sort(sequence2)
    
    __merge(sequence1, sequence2, sequence)

    
def quick_sort(sequence):
    __quick_sort(sequence, 0, len(sequence) - 1)


def sequencer(count=0, step=1):
    while True:
        yield count
        count += step

        
def __merge(sequence1, sequence2, merged_sequence):
    total_length = len(sequence1) + len(sequence2)
    assert len(merged_sequence) == total_length, 'result sequence does not have enough space' 
    
    seq = sequencer()
    while sequence1 and sequence2:
        if sequence1[0] <= sequence2[0]:
            merged_sequence[next(seq)] = sequence1.pop(0)
        else:
            merged_sequence[next(seq)] = sequence2.pop(0)
    while sequence1:
        merged_sequence[next(seq)] = sequence1.pop(0)
    while sequence2:
        merged_sequence[next(seq)] = sequence2.pop(0)


def __quick_sort(sequence, left, right):
    if left >= right:
        return
    else:
        pivot = sequence[right]
        pivot_location = __partition_it(sequence, left, right - 1, pivot)
        __quick_sort(sequence, left, pivot_location - 1)
        __quick_sort(sequence, pivot_location + 1, right)

        
def __partition_it(sequence, left, right, pivot):
    left_seq = sequencer(left)
    right_seq = sequencer(right, step=-1)
    while True:
        left_ptr = next(left_seq)
        right_ptr = next(right_seq)
        while left_ptr < right and sequence[left_ptr] < pivot:
            left_ptr = next(left_seq)
        while right_ptr > left and sequence[right_ptr] > pivot:
            right_ptr = next(right_seq)
        
        if left_ptr >= right_ptr:
            break
        else:
            sequence[left_ptr], sequence[right_ptr] = sequence[right_ptr], sequence[left_ptr]
    if left_ptr != right or sequence[left_ptr] > pivot:
        sequence[left_ptr], sequence[right + 1] = sequence[right + 1], sequence[left_ptr]
        return left_ptr
    else:
        return left_ptr + 1


def tester(sequence_for_sorting, sort_algo, verbose=True):
    if verbose:
        print 'testing {} algorithm'.format(sort_algo.__name__)
        print 'unsorted sequence: {}'.format(sequence_for_sorting)
    sort_algo(sequence_for_sorting)
    if verbose:
        print 'sequence after {}: {}'.format(sort_algo.__name__, sequence_for_sorting)


if __name__ == '__main__':
    
    SETUP_CODE = '''
from random import seed
from random import randint
from sorter import tester

from sorter import bubble_sort 
from sorter import selection_sort 
from sorter import insertion_sort 
from sorter import shell_sort 
from sorter import merge_sort 
from sorter import quick_sort 

seed(1)
sequence = [randint(0, 5000) for _ in range(500)]
    '''
    
    print 'bubble_sort stats: {}'.format(repeat(stmt="tester(sequence, bubble_sort, False)", setup=SETUP_CODE, number=100, repeat=3))
    print 'selection_sort stats: {}'.format(repeat(stmt="tester(sequence, selection_sort, False)", setup=SETUP_CODE, number=100, repeat=3))
    print 'insertion_sort stats: {}'.format(repeat(stmt="tester(sequence, insertion_sort, False)", setup=SETUP_CODE, number=100, repeat=3))
    print 'shell_sort stats: {}'.format(repeat(stmt="tester(sequence, shell_sort, False)", setup=SETUP_CODE, number=100, repeat=3))
    print 'merge_sort stats: {}'.format(repeat(stmt="tester(sequence, merge_sort, False)", setup=SETUP_CODE, number=100, repeat=3))
    print 'quick_sort stats: {}'.format(repeat(stmt="tester(sequence, quick_sort, False)", setup=SETUP_CODE, number=100, repeat=3))

