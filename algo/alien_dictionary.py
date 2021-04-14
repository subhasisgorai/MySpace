from collections import defaultdict
from itertools import izip_longest


def alienOrder(words):

    def find_relation(word_1, word_2, vertices):
        if word_1 and word_2:
            relation = None
            for c1, c2 in izip_longest(word_1, word_2):
                if c1:
                    vertices.add(c1)
                if c2:
                    vertices.add(c2)
                    
                if c1 is not c2 and c1 and c2 and not relation:
                    relation = (c1, c2)
            return relation

    def extract_relations(g):
        vertices = set()
        for i in range(len(words) - 1):
            relation = find_relation(words[i], words[i + 1], vertices)
            if relation:
                g[relation[0]].add(relation[1])
        return vertices

    def _topological_sort_helper(ready_stack, visiting, vertex):
        visiting.add(vertex)
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex in visiting:
                raise ValueError('graph contains cycle')
            if adjacent_vertex not in ready_stack:
                _topological_sort_helper(ready_stack, visiting, adjacent_vertex)
        visiting.remove(vertex)
        ready_stack.append(vertex)

    def topological_sort_dfs():
        ready_stack = list()
        visiting = set()

        for vertex in vertices:
            visiting.clear()
            if vertex not in ready_stack:
                _topological_sort_helper(ready_stack, visiting, vertex)

        return [ready_stack.pop() for _ in range(len(ready_stack))]
    
    def topological_sort():
        topo_order = list()
        ready = list()
        in_order = defaultdict(int)
        
        for adjacency_list in graph.values():
            if adjacency_list:
                for vertex in adjacency_list:
                    in_order[vertex] += 1
        
        for vertex in vertices:
            if in_order[vertex] == 0:
                ready.append(vertex)
                
        while ready:
            vertex = ready.pop()
            topo_order.append(vertex)
            for adjacenct_vertex in graph[vertex]:
                in_order[adjacenct_vertex] -= 1
                if in_order[adjacenct_vertex] == 0:
                    ready.append(adjacenct_vertex)
        
        return topo_order

    lexicographic_order = ''
    if words:
        graph = defaultdict(set)
        vertices = extract_relations(graph)
        
        if vertices:
            if len(vertices) == 1:
                return next(iter(vertices))
            try:
                lexicographic_order = ''.join(topological_sort())
            except:
                print 'cycle detected',
    return lexicographic_order


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
    print_result(["ac","ab","zc","zb"])
    print_result(["ac","ab","zc","zb"])
    print_result(["wrt","wrf","er","ett","rftt","te"])
