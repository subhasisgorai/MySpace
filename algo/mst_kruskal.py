from algo.graph import Graph
from algo.priority_queue import HeapPriorityQueue
from algo.union_find import Partition


def mst_kruskal(g):
    spannning_tree = list()
    forest = Partition()
    positions = dict()
    pq = HeapPriorityQueue()
    
    for v in g.vertices():
        positions[v] = forest.make_group(v)
    
    for e in g.edges():
        pq.add(e.element(), e)
        
    size = g.vertex_count()
    while (len(spannning_tree) != size - 1 
            and not pq.is_empty()):
        edge = pq.remove_min()[1]
        u, v = edge.endpoints()
        a, b = (forest.find(positions[u]),
                    forest.find(positions[v]))
        if a != b:
            spannning_tree.append(edge)
            forest.union(a, b)
    
    return spannning_tree


if __name__ == '__main__':
    g = Graph()
    
    a = g.insert_vertex('a')
    b = g.insert_vertex('b')
    c = g.insert_vertex('c')
    d = g.insert_vertex('d')
    e = g.insert_vertex('e')
    f = g.insert_vertex('f')
    
    g.insert_edge(a, b, 2)
    g.insert_edge(a, c, 3)
    g.insert_edge(b, c, 4)
    g.insert_edge(b, d, 3)
    g.insert_edge(c, e, 2)
    g.insert_edge(d, f, 5)
    g.insert_edge(e, f, 1)
    
    spanning_tree = mst_kruskal(g)
    print spanning_tree

