from itertools import islice
import heapq


def top_k(k, stream):
    min_heap = [(len(str_item), str_item) for str_item in islice(stream, k)]
    heapq.heapify(min_heap)
    for new_item in stream:
        if  new_item and len(min_heap[0]) < new_item:
            heapq.heappushpop(min_heap, (len(new_item), new_item)) 
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


sample_sentence = '''At first this was an odd turn of
    phrase, we introduce Dave as one of our leading 
    architects'''


def str_len_comparator(str_1, str_2):
    if len(str_1) < len(str_2):
        return -1
    elif len(str_1) == len(str_2):
        return 0
    else:
        return 1

    
str_stream = sample_sentence.split()
str_stream.sort(cmp=str_len_comparator, reverse=True)
for i in str_stream:
    print i

print top_k(9, iter(str_stream))
