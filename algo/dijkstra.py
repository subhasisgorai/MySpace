from ds.adaptable_q import AdaptableHeapPriorityQueue
from ds.graph import Graph


def shortest_path_lengths(g, src):
    d = dict()
    cloud = dict()
    pq = AdaptableHeapPriorityQueue()
    pq_locator = dict()
    
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')
        pq_locator[v] = pq.add(d[v], v)
        
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key
        del pq_locator[u]
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v not in cloud:
                wgt = e.element()
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pq_locator[v], d[v], v) 
                        
    return cloud


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
    
    result_cloud = shortest_path_lengths(g, a)
    print result_cloud
    
    g = Graph(directed=True)
    
    a = g.insert_vertex('a')
    b = g.insert_vertex('b')
    
    g.insert_edge(a, b, 3)
    g.insert_edge(b, a, 2)
    
    result_cloud = shortest_path_lengths(g, a)
    print result_cloud
