from collections import defaultdict


def alienOrder(words):
    lexicographical_order = ''
    
    if words:

        def extract_relations(g):
            for i in range(len(words) - 1):
                current_word, next_word = words[i], words[i + 1]
                if current_word and next_word:
                    for c1, c2 in zip(current_word, next_word):
                        if c1 and c2 and c1 is not c2:
                            if c2 not in g[c1]:
                                g[c1].add(c2)
                                in_order[c2] += 1
                            break
                    else:
                        if len(current_word) > len(next_word):
                            raise ValueError('can not for lexicographical ordering' + 
                                'for the given words')
        
        def topological_ordering(in_order):
            ready = list()
            topo_order = list()
            
            for vertex in vertices:
                if in_order[vertex] == 0:
                    ready.append(vertex)
            
            while ready:
                vertex = ready.pop()
                topo_order.append(vertex)
                for adjacent_vertex in graph[vertex]:
                    in_order[adjacent_vertex] -= 1
                    if in_order[adjacent_vertex] == 0:
                        ready.append(adjacent_vertex)
            
            return topo_order
            
        graph = defaultdict(set)
        in_order = defaultdict(int)
        
        vertices = reduce(lambda s1, s2: s1.union(s2), map(set, filter(lambda word: word, words)), set())
        try:
            extract_relations(graph)
            result = ''.join(topological_ordering(in_order))
            if len(result) == len(vertices):
                lexicographical_order = result
        except:
            pass
    
    return lexicographical_order


if __name__ == '__main__':

    def print_result(sample):
        print 'Output for {}:[{}]'.format(sample, alienOrder(sample))
    
    print_result(["wrt", "wrf", "er", "ett", "rftt"])
    print_result(["z", "x"])
    print_result(["z", "x", "z"])
    print_result(["z", "z"])
    print_result(["ab", "adc"])
    print_result(["a", "b", "ca", "cc"])
    print_result(["abc", "ab"])
    print_result(["wrt", "wrtkj"])
    print_result(["ac", "ab", "zc", "zb"])
    print_result(["wrt","wrf","er","ett","rftt","te"])
