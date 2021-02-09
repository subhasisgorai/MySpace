from copy import deepcopy

from algo.graph import Graph


def floyd_warshall(g):
    closure = deepcopy(g)
    vertices = list(closure.vertices())
    n = len(vertices)
    for k in range(n):
        for i in range(n):
            if i != k and closure.get_edge(vertices[i], vertices[k]) is not None:
                for j in range(n):
                    if i != j != k and closure.get_edge(vertices[k], vertices[j]) is not None:
                        if closure.get_edge(vertices[i], vertices[j]) is None:
                            closure.insert_edge(vertices[i], vertices[j])
        
    return closure


g = Graph()

a = g.insert_vertex('a') 
b = g.insert_vertex('b') 
c = g.insert_vertex('c') 
d = g.insert_vertex('d') 
e = g.insert_vertex('e') 
f = g.insert_vertex('f')

g.insert_edge(a, b)
g.insert_edge(a, c)
g.insert_edge(b, c)
g.insert_edge(b, d)
g.insert_edge(c, e)
g.insert_edge(d, f)
g.insert_edge(e, f)

closure = floyd_warshall(g)
print closure.get_edge(a, f) 
 
