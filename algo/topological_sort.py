from algo.graph import Graph


def topological_sort(graph):
    topo = list()
    ready = list()
    in_count = dict()
    for u in graph.vertices():
        in_count[u] = graph.degree(u, False)
        if in_count[u] == 0:
            ready.append(u)
    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in graph.incident_edges(u):
            v = e.opposite(u)
            in_count[v] -= 1
            if in_count[v] == 0:
                ready.append(v)
    return topo


g = Graph(directed=True)

a = g.insert_vertex('a') 
b = g.insert_vertex('b') 
c = g.insert_vertex('c') 
d = g.insert_vertex('d') 
e = g.insert_vertex('e') 
f = g.insert_vertex('f')

g.insert_edge(a, b)
g.insert_edge(a, c)
g.insert_edge(c, f)
g.insert_edge(d, e)
g.insert_edge(e, f)

topo_order = topological_sort(g)
print topo_order
